from function.lcu_request import lcu_request
import json

def getCurrentSummoner():
    return json.loads(lcu_request("GET", "/lol-summoner/v1/current-summoner"))