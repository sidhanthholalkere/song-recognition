import librosa
from pathlib import Path

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
    
    recorded_audio, _ = librosa.load("data/BP_ET_minor.ogg", sr=SAMPLING_RATE, mono=True)

    return recorded_audio