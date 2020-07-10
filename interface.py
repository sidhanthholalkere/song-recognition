from scipy.ndimage.filters import maximum_filter
from scipy.ndimage.morphology import generate_binary_structure, binary_erosion
from scipy.ndimage.morphology import iterate_structure
import audio_to_spectrogram
import database
import fingerprint
import finding_peaks
#import (what we name the input file)
import testing

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
    audio = #(what we name the input file).mic_to_samples(time)
else:
    path = input("Enter the path of the mp3 file")
    audio = #(what we name the input file).mp3_to_samples(path)

spectogram = audio_to_spectrogram(44100, audio)
threshhold = threshhold_value(spectogram)
temp_neighborhood = generate_binary_structure(2, 1)
neighborhood = iterate_structure(temp_neighborhood, 3)
local_peaks = local_peak_locations(spectogram, )
fanout_num=15
fingerprints = fingerprint(local_peaks, fanout_num)

if user_choice == 1:
    SongDatabase.store_fingerprint(fingerprints, song_name)
elif user_choice == 2:
    SongDatabase.query_fingerprint(fingerprints)












