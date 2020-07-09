import numpy as np
import librosa
import pickle


def query():
    """ Checks the song database to see if song matches

    Parameters
    ----------

    Returns
    -------

    """
    # loads dictionary/database of songs
    database = pickle.load(open("", "rb")) # TO DO: add dictionary file name

    database = {"song_1": 1, "song_2": 2}

    #stores all the tallies in form of {(song-ID, offset): count} where count is the tally
    tally = {}

    # the fingerprints for the song checking into database to find match
    check_song_fingerprints = np.array(([1,2])) # TO DO: use finger print function

    for f1, f2, dt in check_song_fingerprints:
        corresponding_freq_t = database.get(tuple(f1, f2, dt)) # list of (song-ID, t)
        times = np.array([freq_t[-1] for freq_t in corresponding_freq_t]) # np.array of times
        songs = np.array([freq_t[0] for freq_t in corresponding_freq_t]) #
        offset = times - dt

    #TO DO - add to dictionary (song-ID, offset): count
    
    #ADD RETURN STATEMENT