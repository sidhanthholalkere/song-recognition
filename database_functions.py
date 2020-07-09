# storing fingerprint
# querying fingerprint
song_database = dict()


def store_fingerprint(fingerprints, song_id):
    """
    takes a list of fingerprints of a song and the song's ID, adds the prints and ID to database
    Parameters
    ----------
        fingerprints : List[Tuple(float, float, float)]
            list of freq of initial peak, freq of peak fanned out to, time gap between peaks
        song_id : str
            ID of song the fingerprints are taken from
    """
    for (fm, fn, dt), tm in fingerprints:
        if (fm, fn, dt) not in song_database:
            song_database[(fm, fn, dt)] = [(song_id, tm)]
        else:
            song_database[(fm, fn, dt)].append((song_id, tm))


def query_fingerprint(fingerprint):
    """
    takes a fingerprint (f1, f2, relative_time), matches to database key and tallies which song has highest tally
    Parameters
    ----------
        fingerprint : Tuple(float, float, float)
            freq of initial peak, freq of peak fanned out to, time gap between peaks
    Returns
    -------
        song_ID : str
            ID of song with the highest tally (most closely matches fingerprint)
    """
    t_rel = fingerprint[-1]

    if fingerprint in song_database:
        poss_songs = song_database[fingerprint]
        tally = dict()
        for song_id, t_abs in poss_songs:
            t_offset = t_abs - t_rel
            if (song_id, t_offset) in tally:
                tally[(song_id, t_offset)] += 1
            else:
                tally[(song_id, t_offset)] = 1
        sorted_tally = sorted(tally.items(), key=lambda kv: kv[1])
        return sorted_tally[0[0]]
    else:
        return 'not in database'
