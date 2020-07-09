import librosa
import numpy as np
from pathlib import Path
from microphone import record_audio

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

    return recorded_audio

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