import json
import os
from utils.championFilter import championFilter
import requests


# Load the filtered data from the JSON file into a dictionary
if not os.path.exists("C:/LongDev/LongRunes/champion.json"):
        leagueVersion = json.loads(requests.get(f'https://ddragon.leagueoflegends.com/api/versions.json').text)
        #index 0 for the latest version
        leagueVersion = leagueVersion[0]
        print("Champion data not found, getting data from ddragon server")
        championFilter(leagueVersion)
with open('C:/LongDev/LongRunes/champion.json', 'r') as f:
    filtered_data = json.load(f)

def querryChampion(id):
    return filtered_data[str(id)]