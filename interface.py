from scipy.ndimage.filters import maximum_filter
from scipy.ndimage.morphology import generate_binary_structure, binary_erosion
from scipy.ndimage.morphology import iterate_structure
import utils
import database

print("Add to song database or try to match song?")
print("1: Add to song database")
user_choice = input("2: Match Song")
if user_choice == 1:
    song_name = input("Enter the song name")
print("Use the mic or mp3")
print("1: Use mic")
method = input("2: Use mp3")


if (method == 1):
    time = input("Enter the length of the song")
    audio = utils.mic_to_samples(time)
else:
    path = input("Enter the path of the mp3 file")
    audio = utils.mp3_to_samples(path)

spectogram = utils.audio_to_spectrogram(44100, audio)
threshhold = utils.threshhold_value(spectogram)
temp_neighborhood = generate_binary_structure(2, 1)
neighborhood = iterate_structure(temp_neighborhood, 3)
local_peaks = utils.local_peak_locations(spectogram, )
fanout_num=15
fingerprints = utils.fingerprint(local_peaks, fanout_num)

if user_choice == 1:
    database.SongDatabase.store_fingerprint(fingerprints, song_name)
elif user_choice == 2:
    database.SongDatabase.query_fingerprint(fingerprints)


# revised interface:
'''
print("Add to song database or try to match song?")
print("1: Add to song database")
user_choice = input("2: Match Song")
if user_choice == 1:
    song_name = input("Enter the song name")
print("Use the mic or mp3")
print("1: Use mic")
method = input("2: Use mp3")

if user_choice == 1: (store song)
    pass song_name and method to database.store_song
    database stores song_name, does lines 24-30 to generate fingerprints
    stores the generated fingerprints
else: (query song)
    pass method to database.query_song
    database does lines 24-30 to generate the fingerprint
    checks database for song with highest tally
    returns song name with highest tally
'''








