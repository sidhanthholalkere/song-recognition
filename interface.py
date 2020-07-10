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

fingerprints = utils.spectogram_to_fingerprint(audio)

if user_choice == 1:
    database.SongDatabase.store_fingerprint(fingerprints, song_name)
elif user_choice == 2:
    database.SongDatabase.query_fingerprint(fingerprints)












