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

