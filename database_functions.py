# storing fingerprint
# querying fingerprint
song_database = dict()


def store_fingerprint(fingerprints, song_id):
    """
        takes a list of fingerprints of a song and the song's ID, adds the prints and ID to database
        Parameters
        ----------
            fingerprints : List[Tuple(float, float, float)]
                (freq of initial peak, freq of peak fanned out to, time gap between peaks
            song_id : str
                ID of song the fingerprints are taken from
    """
    for (fm, fn, dt), tm in fingerprints:
        if (fm, fn, dt) not in song_database:
            song_database[(fm, fn, dt)] = [(song_id, tm)]
        else:
            song_database[(fm, fn, dt)].append((song_id, tm))


def query_fingerprint(fingerprint):
    if fingerprint in song_database:

    pass
