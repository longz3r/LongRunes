from function.querryChampion import querryChampion
from function.getRune import getRune
from function.lcu_request import lcu_request

import json

def applyRune(championId):
    championName = querryChampion(championId)
    print("Applying runes for", championName)
    runes = getRune(championName)

    pages = lcu_request("GET", "/lol-perks/v1/pages")
    pages = json.loads(pages)

    if len(pages) == 0:
        #create page function
        print("Create page")
        lcu_request("POST", "/lol-perks/v1/pages/", runes)
    else:
        #update page
        currentPage = lcu_request("GET", "/lol-perks/v1/currentpage")
        currentPage = json.loads(currentPage)
        lcu_request("PUT", f"/lol-perks/v1/pages/{currentPage['id']}", runes)