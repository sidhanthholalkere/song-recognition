from scipy.ndimage.filters import maximum_filter
from scipy.ndimage.morphology import generate_binary_structure, binary_erosion
from scipy.ndimage.morphology import iterate_structure
import utils
import database

print("Add to song database or try to match song?")
print("1: Add to song database")
user_choice = input("2: Match Song")
song_name = ""
if user_choice == 1:
    song_name = input("Enter the song name")
print("Use the mic or mp3")
print("1: Use mic")
method = input("2: Use mp3")


if (method == 1):
    time = input("Enter the length of the song")
    audio = utils.mic_to_samples(int(time))
else:
    path = input("Enter the path of the mp3 file")
    audio = utils.mp3_to_samples(path)

spectogram, frequency, midpoint = utils.audio_to_spectogram(44100, audio)
threshhold = utils.threshold_value(spectogram)
temp_neighborhood = generate_binary_structure(2, 1)
neighborhood = iterate_structure(temp_neighborhood, 3)
local_peaks = utils.local_peak_locations(spectogram, neighborhood, threshhold)
fanout_num=15
fingerprints = utils.generate_fingerprint(local_peaks, fanout_num)

if user_choice == 1:
    database.SongDatabase.store_fingerprint(fingerprints, song_name)
elif user_choice == 2:
    database.SongDatabase.query_fingerprint(fingerprints)












