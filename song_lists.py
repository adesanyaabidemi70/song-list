print("hey there user what song may we help you with today?")
user_song = input()

list_of_songs = {"ginger me", 'dumebi', 'ku lo sa', 'electricity', 'DKT', 'hello mate', 'iron man'}

new_song = set(list_of_songs)
list_of_songs.add(user_song)

for song in list_of_songs:
    print(song, sep="\n")
# print(list_of_songs)
