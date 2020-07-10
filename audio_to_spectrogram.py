import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab


def audio_to_spectogram(sampling_rate, audio):
<<<<<<< HEAD

    Spectrum, freqs, midpoint_times = mlab.specgram(audio,
                                            NFFT=4096, 
                                            Fs=sampling_rate, 
                                            noverlap=4096 // 2, # number points of overlap between blocks. 
                                            mode='magnitude', #returns the magnitude spectrum
                                            
                                            ) 
                                            
                                             
                                            
    return Spectrum , freqs, midpoint_times


    """
    turns audio into spectograph

=======
    """Converts audio samples to a spectogram
>>>>>>> a7dc13e9050780e2277bfef00ee9c83781f827b9
    Parameters
    ----------
    sampling_rate : int, 
        the sampling rate

    audio : np.array
<<<<<<< HEAD
    the audio samples
=======
        the audio from the microphone
>>>>>>> a7dc13e9050780e2277bfef00ee9c83781f827b9


    Returns
    -------
    Spectrum: 2-D array
        spectograph, colluma
    
    freqs: 1-D array 
        corresponding frequencies

    midpoint_times : 1-D array
<<<<<<< HEAD
    correspinding times of the middle of each window
    
    """
=======
        corresponding times of the middle of each window
    """

    Spectrum, freqs, midpoint_times = mlab.specgram(audio,
                                            NFFT=4096, 
                                            Fs=sampling_rate, 
                                            noverlap=4096 // 2, # number points of overlap between blocks. 
                                            mode='magnitude', #returns the magnitude spectrum
                                            
                                            ) 
                                            
                                             
                                            
    return Spectrum , freqs, midpoint_times


    
>>>>>>> a7dc13e9050780e2277bfef00ee9c83781f827b9
