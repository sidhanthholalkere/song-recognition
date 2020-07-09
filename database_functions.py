# storing fingerprint
# querying fingerprint
song_database = dict()


def store_fingerprint(fanout_m, song_id):
    for (fm, fn, dt), tm in fanout_m:
        if (fm, fn, dt) not in song_database:
            song_database[(fm, fn, dt)] = [(song_id, tm)]
        else:
            song_database[(fm, fn, dt)].append((song_id, tm))


def query_fingerprint(fingerprint):
    pass
