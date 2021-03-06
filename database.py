import pickle
from pathlib import Path
import utils


class SongDatabase:
    """A database that stores 'fingerprints' of songs
    """

    def __init__(self):
        """Initializes a song database
        """
        # fingerprints is a dict with fingerprints as the key
        # and songs as the values
        self.fingerprints = {}
        # songs contains a list of songs
        self.songs = []

    def store_song(self, song_name, recording_method):
        """
        takes a song, generates the fingerprints, adds all this to the respective dict/list
        Parameters
        ----------
            song_name : str
                name of song the fingerprints are taken from
            recording_method : int (1, 2)
                user's choice for method of recording; 1 for mic, 2 for mp3
        """
        self.songs.append(song_name)
        song_id = self.songs.index(song_name)

        if recording_method == 1:
            time = input("Enter the length of the song")
            time = int(time)
            audio = utils.mic_to_samples(time)
        else:
            path = input("Enter the path of the mp3 file")
            audio = utils.mp3_to_samples(path)

        fingerprints = utils.spectrogram_to_fingerprint(audio)

        for (fm, fn, dt), t_abs in fingerprints:
            if (fm, fn, dt) not in self.fingerprints:
                self.fingerprints[(fm, fn, dt)] = [(song_id, t_abs)]
            else:
                self.fingerprints[(fm, fn, dt)].append((song_id, t_abs))

    def query_song(self, recording_method):
        """
        takes in recording_method (either mic or mp3), gets fingerprint sequence for the queried song, returns song name
        Parameters
        ----------
            recording_method : int (1, 2)
                user's choice for method of recording; 1 for mic, 2 for mp3
        Returns
        -------
            song_ID : str
                ID of song with the highest tally (most closely matches fingerprint)
        """
        threshold_success = 50  # song must have at least 50 tallies to be a success
        threshold_percentage = 0.75  # song must have 75% of total tallies

        if recording_method == 1:
            time = input("Enter the length of the song")
            time = int(time)

            audio = utils.mic_to_samples(time)
        else:
            path = input("Enter the path of the mp3 file")
            audio = utils.mp3_to_samples(path)

        q_fingerprints = utils.spectrogram_to_fingerprint(audio)
        tally = dict()

        for (fm, fn, dt), t_rel in q_fingerprints:
            if (fm, fn, dt) in self.fingerprints:
                poss_songs = self.fingerprints[(fm, fn, dt)]
                for song_id, t_abs in poss_songs:
                    t_offset = t_abs - t_rel
                    tally[(song_id, t_offset)] = tally.get((song_id, t_offset), 0) + 1
            else:
                return 'not in database'

        # sorted_tally is a list of tuples in order of tallies, from greatest to least [( (songID, t_off), tally ), ...]
        # sorted_tally[0][0][0] gives the song ID of the song w greatest # of tallies
        # pass this to self.songs to retrieve the song name
        sorted_tally = sorted(tally.items(), key=lambda kv: kv[1], reverse=True)
        total_tallies = sum(tally.values())
        greatest_tally = sorted_tally[0][-1]
        print(greatest_tally)
        second_greatest_tally = sorted_tally[1][-1]
        print(second_greatest_tally)
        print(sorted_tally[:10])

        if greatest_tally >= threshold_success and greatest_tally > second_greatest_tally * 10:
            return self.songs[sorted_tally[0][0][0]]
        else:
            return 'did not meet threshold of successful classification'

    def load_database(self, path):
        """
        takes in the path of the database, and returns loaded database
        ----------
            path: String
                The path of the database
        Returns
        -------
            database : Dict
                ID of song with the highest tally (most closely matches fingerprint)
        """
        # loads dictionary/database of songs
        path = Path(path)
        with open(path, mode="rb") as opened_file:
            return pickle.load(opened_file)

        return 'file does not exist'

    def save_database(self, filename):
        """
        takes in the name of file you want to save to, pickles the database object and saves to that file
        ----------
            filename: String
                the name of the file
        """
        with open(filename, mode="wb") as opened_file:
            return pickle.dump(self, opened_file)

        #file = open(filename, 'wb')
        #pickle.dump(self, file)