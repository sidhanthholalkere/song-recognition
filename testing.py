import numpy as np
import random as random

SAMPLING_RATE = 44100


def test_mp3(path, random_noise=False, random_slice=False):

    song_samples = mp3_to_samples(path)


    if (random_noise):
        fourier = np.fft.rfft(song_samples)
        

        #amps, phases = fourier_complex_to_real(fourier, fourier.shape[0])
    
        amps = np.mean(song_samples)    
    
        noise = np.random.normal(amps, 200000, fourier.shape)

                        
        song_samples = np.fft.irfft(np.add(fourier, noise))
       

        
    
        if (random_slice):
            index = random.uniform(0,song_samples.shape[0]-SAMPLING_RATE)
            index = round(index)

                
            size_slice = random.uniform(index+SAMPLING_RATE, song_samples.shape[0])

        
            size_slice = round(size_slice-SAMPLING_RATE)
    
        

        
            return(song_samples[index:index+size_slice])
        else:
            return song_samples
        #add random noise

    elif (random_slice):
            index = np.random.random_sample() * (song_samples.shape[0]-SAMPLING_RATE)
            index = round(index)

        
            random = np.random.random_sample()
        
            size_slice = random * (song_samples.shape[0]-index)

        
            size_slice = round(size_slice)
        
        
            return(song_samples[index:index+size_slice])
    else:
        return song_samples



    """
    adds noise/cuts songs into pieces from a file

    Parameters
    ----------
    path : str
    string of the mp3 file

    random_noise : boolean
    True if want to apply random noise to function

    random_slice : boolean
    True if we wanr to take a random slice from the song

    Returns
    -------
    
    tranformed song : np.array
    sampled of the song with noise/cut
    
    """

def fourier_complex_to_real(complex_coeffs, N):
    """
    Converts complex-valued Fourier coefficients (of 
    real-valued data) to the associated amplitudes and 
    phase-shifts of the real-valued sinusoids
    
    Parameters
    ----------
    complex_coeffs : numpy.ndarray, shape-(N//2 + 1,)
        The complex valued Fourier coefficients for k=0, 1, ...
    
    N : int
        The number of samples that the DFT was performed on.
    
    Returns
    -------
    Tuple[numpy.ndarray, numpy.ndarray]
        (amplitudes, phase-shifts)
        Two real-valued, shape-(N//2 + 1,) arrays
    """
    amplitudes = np.abs(complex_coeffs) / N

    # |a_k| = 2 |c_k| / N for all k except for
    # k=0 and k=N/2 (only if N is even)
    # where |a_k| = |c_k| / N
    amplitudes[1 : (-1 if N % 2 == 0 else None)] *= 2

    phases = np.arctan2(-complex_coeffs.imag, complex_coeffs.real)
    return amplitudes, phases


def test_from_mic(time, random_noise, random_slice):

    """
    adds noise/cuts songs into pieces from mic

    Parameters
    ----------
    time : int
    amount of time you want to record

    random_noise : boolean
    True if want to apply random noise to function

    random_slice : boolean
    True if we wanr to take a random slice from the song

    Returns
    -------
    
    tranformed song : np.array
    sampled of the song with noise/cut
    
"""

    song_samples = mic_to_samples(time)

    if (random_noise):
        fourier = np.fft.rfft(song_samples)
        

        #amps, phases = fourier_complex_to_real(fourier, fourier.shape[0])
    
        amps = np.mean(song_samples)    
    
        noise = np.random.normal(amps, 200000, fourier.shape)

                        
        song_samples = np.fft.irfft(np.add(fourier, noise))
        
    
        if (random_slice):
            index = random.uniform(0,song_samples.shape[0]-SAMPLING_RATE)
            index = round(index)

                
            size_slice = random.uniform(index+SAMPLING_RATE, song_samples.shape[0])

        
            size_slice = round(size_slice-SAMPLING_RATE)
    
        

        
            return(song_samples[index:index+size_slice])
        

        
            return(song_samples[index:index+size_slice])
        else:
            return song_samples

    elif (random_slice):
            index = np.random.random_sample() * (song_samples.shape[0]-44100)
            index = round(index)

        
            random = np.random.random_sample()
        
            size_slice = random * (song_samples.shape[0]-index)

        
            size_slice = round(size_slice)
        
        
            return(song_samples[index:index+size_slice])
    else:
        return song_samples

        
