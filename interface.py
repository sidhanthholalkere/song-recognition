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

if user_choice == 1:
    database.SongDatabase.store_song(song_name, method)
elif user_choice == 2:
    database.SongDatabase.query_song(method)


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








