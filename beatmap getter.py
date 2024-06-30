import os, re, json

osu_path = ""
songs = os.listdir(osu_path)
print(print(len(songs)))
songs_string = ""
for song in songs:
    songs_string += (song + "\n")
beatmap_ids = re.findall(r"""\d{3,6}""", songs_string)
dictionary = {"length" : len(beatmap_ids), "ids" : beatmap_ids}
dictionary = json.dumps(dictionary)
print(len(beatmap_ids))
with open("all_beatmaps.txt", "w") as file:
    file.write(dictionary)