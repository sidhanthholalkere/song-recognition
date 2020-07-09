# a SongDatabase has a dictionary called fingerprints, and a list of songs.
# fingerprints stores fingerprint as key and song ID as the value
# the song ID corresponds to a song in the song list

# song_database example: { (fm, fn, dt) : [(song_id, tm), (), () ...] }


song_database = SongDatabase()


def store_fingerprint(fingerprints, song_name):
    """
    takes a list of fingerprints of a song and the song's ID, adds the prints and ID to database
    Parameters
    ----------
        fingerprints : List[Tuple(float, float, float)]
            list of freq of initial peak, freq of peak fanned out to, time gap between peaks
        song_name : str
            name of song the fingerprints are taken from
    """
    song_database.songs.append(song_name)
    song_id = song_database.songs.index(song_name)

    for (fm, fn, dt), tm in fingerprints:
        if (fm, fn, dt) not in song_database.fingerprints:
            song_database.fingerprints[(fm, fn, dt)] = [(song_id, tm)]
        else:
            song_database.fingerprints[(fm, fn, dt)].append((song_id, tm))


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

    if fingerprint in song_database.fingerprints:
        poss_songs = song_database.fingerprints[fingerprint]
        tally = dict()
        for song_id, t_abs in poss_songs:
            t_offset = t_abs - t_rel
            if (song_id, t_offset) in tally:
                tally[(song_id, t_offset)] += 1
            else:
                tally[(song_id, t_offset)] = 1
        # sorted_tally is a list of tuples in order of tallies, from greatest to least [( (songID, t_off), tally ), ...]
        # sorted_tally[0[0]] gives the song ID of the song w greatest # of tallies
        # pass this to song_database.songs to retrieve the song name
        sorted_tally = sorted(tally.items(), key=lambda kv: kv[1], reverse=True)
        return song_database.songs[sorted_tally[0[0]]]
    else:
        return 'not in database'
