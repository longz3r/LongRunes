import os
from utils.runeFilter import runeFilter
from utils.championFilter import championFilter
import requests
import json
from inputimeout import inputimeout, TimeoutOccurred

def askUpdate(leagueVersion:str):
    try:
        answer = inputimeout(prompt='Do you want to update runes and champion data (Y/n)', timeout=15)
    except TimeoutOccurred:
        answer = None
    if answer != None:
        answer = answer.lower().strip()
        if answer == "":
            print("Updating runes and champion data")
            championFilter(leagueVersion)
            runeFilter(leagueVersion)
        elif answer == "yes" or answer == "y":
            print("Updating runes and champion data")
            championFilter(leagueVersion)
            runeFilter(leagueVersion)
        elif answer == "no" or answer == "n":
            print("Not updating runes and champion data")
        else:
            print("Invalid answer (Y/N/Yes/No)")
            askUpdate(leagueVersion)
    else:
        print("No answer in 15 seconds, starting LongRunes without update runes and champion data")


def startup():
    print("Getting version information")
    leagueVersion = json.loads(requests.get(f'https://ddragon.leagueoflegends.com/api/versions.json').text)
    #index 0 for the latest version
    leagueVersion = leagueVersion[0]
    print("Current League of Legends version:", leagueVersion)
    if not os.path.exists("C:/LongDev"):
        os.mkdir("C:/LongDev")
    if not os.path.exists("C:/LongDev/LongRunes"):
        os.mkdir("C:/LongDev/LongRunes")
    if not os.path.exists("C:/LongDev/LongRunes/runes.json"):
        print("Runes data not found, getting data from ddragon server")
        runeFilter(leagueVersion)
    if not os.path.exists("C:/LongDev/LongRunes/champion.json"):
        print("Champion data not found, getting data from ddragon server")
        championFilter(leagueVersion)

    championVersion = open("C:/LongDev/LongRunes/champion.json", "r")
    championVersion = json.load(championVersion)["version"]

    runesVersion = open("C:/LongDev/LongRunes/runes.json", "r")
    runesVersion = json.load(runesVersion)["version"]

    print("Current runes data version:", runesVersion)
    print("Current champion data version:", championVersion)

    askUpdate(leagueVersion)


