import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab


def audio_to_spectogram():
    def audio_to_spectogram(sampling_rate, audio):
    
    Spectrum, freqs, midpoint_times, image = ax.specgram(audio,
                                             NFFT=4096, # num data points each block for the FFT.
                                             Fs=sampling_rate) #sampling frequency
                                            
                                             
                                            
    return Spectrum , freqs, midpoint_times


    """
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
    correspinding times of the middle of each window

    Examples
    --------
    
    
    """