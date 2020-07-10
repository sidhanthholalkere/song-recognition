import librosa
import numpy as np
import matplotlib.mlab as mlab
from pathlib import Path
from microphone import record_audio
from numba import njit
from scipy.ndimage.morphology import generate_binary_structure
from scipy.ndimage.morphology import iterate_structure


SAMPLING_RATE = 44100

def mp3_to_samples(path):
    """Converts audio from an mp3 file into samples

    Parameters
    ----------
    path : str
        The path of the mp3 file we wish to convert.

    Returns
    -------
    recorded_audio : np.array
        The audio samples from the mp3
    """

    path = Path(path)
    
    recorded_audio, _ = librosa.load(path, sr=SAMPLING_RATE, mono=True)
    
    return recorded_audio * 2**15

def mic_to_samples(time):
    """Converts audio from micropgone input into samples

    Parameters
    ----------
    time : int
        The duration the microphone should record for.

    Returns
    -------
    recorded_audio : np.array
        The audio samples from the microphone input
    """

    frames, sample_rate = record_audio(time)

    recorded_audio = np.hstack([np.frombuffer(i, np.int16) for i in frames])

    return recorded_audio

def audio_to_spectrogram(sampling_rate, audio):
    """Converts audio samples to a spectogram
    Parameters
    ----------
    sampling_rate : int, 
        the sampling rate

    audio : np.array
        the audio from the microphone


    Returns
    -------
    Spectrum: 2-D array
        spectograph, colluma
    
    freqs: 1-D array 
        corresponding frequencies

    midpoint_times : 1-D array
        corresponding times of the middle of each window
    """

    Spectrum, freqs, midpoint_times = mlab.specgram(audio,
                                            NFFT=4096, 
                                            Fs=sampling_rate, 
                                            noverlap=4096 // 2, # number points of overlap between blocks. 
                                            mode='magnitude', #returns the magnitude spectrum
                                            
                                            ) 
                                            
                                             
                                            
    return Spectrum , freqs, midpoint_times

def threshold_value(data_2d, percentile=75):
    """Returns a threshold based on the given percentile

    Parameters
    ----------
    data_2d: np.array
        A spectogram

    percentile: float
        Percentile to threshold by

    Returns
    -------
    float
        Returns the proper threshold
    """
    data = np.copy(data_2d).flatten()
    # third quartile will be an underestimate if array is not divisible by 4
    # third_quartile = len(flattened) * 3 // 4 - 1 # 75% for indexing, subtracting 1 bc index starts at 0
    return np.percentile(data, percentile)

@njit
def _peaks(data_2d, rows, cols, amp_min):
    """
    A Numba-optimized 2-D peak-finding algorithm.
    
    Parameters
    ----------
    data_2d : numpy.ndarray, shape-(H, W)
        The 2D array of data in which local peaks will be detected.

    rows : numpy.ndarray, shape-(N,)
        The 0-centered row indices of the local neighborhood mask
    
    cols : numpy.ndarray, shape-(N,)
        The 0-centered column indices of the local neighborhood mask
        
    amp_min : float
        All amplitudes at and below this value are excluded from being local 
        peaks.
    
    Returns
    -------
    List[Tuple[int, int]]
        (row, col) index pair for each local peak location. 
    """
    peaks = []
    
    # iterate over the 2-D data in col-major order
    for c, r in np.ndindex(*data_2d.shape[::-1]):
        if data_2d[r, c] <= amp_min:
            continue

        for dr, dc in zip(rows, cols):
            # don't compare element (r, c) with itself
            if dr == 0 and dc == 0:
                continue

            # mirror over array boundary
            if not (0 <= r + dr < data_2d.shape[0]):
                dr *= -1

            # mirror over array boundary
            if not (0 <= c + dc < data_2d.shape[1]):
                dc *= -1

            if data_2d[r, c] < data_2d[r + dr, c + dc]:
                break
        else:
            peaks.append((r, c))
    return peaks

def local_peak_locations(data_2d, neighborhood, amp_min):
    """
    Defines a local neighborhood and finds the local peaks
    in the spectrogram, which must be larger than the specified `amp_min`.
    
    Parameters
    ----------
    data_2d : numpy.ndarray, shape-(H, W)
        The 2D array of data in which local peaks will be detected
    
    neighborhood : numpy.ndarray, shape-(h, w)
        A boolean mask indicating the "neighborhood" in which each
        datum will be assessed to determine whether or not it is
        a local peak. h and w must be odd-valued numbers
        
    amp_min : float
        All amplitudes at and below this value are excluded from being local 
        peaks.
    
    Returns
    -------
    List[Tuple[int, int]]
        (row, col) index pair for each local peak location.
    
    Notes
    -----
    The local peaks are returned in column-major order.
    """
    rows, cols = np.where(neighborhood)
    assert neighborhood.shape[0] % 2 == 1
    assert neighborhood.shape[1] % 2 == 1

    # center neighborhood indices around center of neighborhood
    rows -= neighborhood.shape[0] // 2
    cols -= neighborhood.shape[1] // 2
    
    return _peaks(data_2d, rows, cols, amp_min=amp_min)

def generate_fingerprint(peaks, fanout_num):
    """Generates a fingerprint based off a spectograms peaks

    Parameters
    ----------
    peaks : List[Tuple[int, int]]
        (row, col) index pair for each local peak location

    fanout_num : int
        number of peaks to connect to

    Return
    ------
    fingerprint : List[Tuple(float, float, float)]
        (freq of initial peak, freq of peak fanned out to, time elapsed between peaks
    """
    fingerprint = []
    for index in range(len(peaks) - 1):
        for i in range(fanout_num):
            if index+i+1<len(peaks):
                fingerprint.append(((peaks[index][0], peaks[index + i + 1][0], peaks[index + i + 1][1] - peaks[index][1]), peaks[index][1]))
    return fingerprint

def spectogram_to_fingerprint(audio):
    """
    Puts the rest of the functions together
    Parameters
    ----------
    audio : audio samples from either microphone or mp3

    Returns
    -------
    fingerprint: List[Tuple(float, float, float)]
        list of fingerprints for the song

    """
    spectrogram, frequency, midpoint = audio_to_spectrogram(44100, audio)
    threshhold = threshold_value(spectrogram)
    temp_neighborhood = generate_binary_structure(2, 1)
    neighborhood = iterate_structure(temp_neighborhood, 3)
    local_peaks = local_peak_locations(spectrogram, neighborhood, threshhold)
    fanout_num = 15
    fingerprints = generate_fingerprint(local_peaks, fanout_num)
    return fingerprints
