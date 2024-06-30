import json, requests
from ossapi import Ossapi as osuapi

with open("all_beatmaps.txt", "r") as file:
    all_beatmap_ids = json.load(file)["ids"]

beatmap = requests.get("https://osu://dl/" + all_beatmap_ids[30], params = {"k":""})