from function.querryChampion import querryChampion
from function.getRune import getRune
from function.lcu_request import lcu_request

def applyRune(championId):
    championName = querryChampion(championId)
    runes = getRune(championName)
    print(runes)

    pages = lcu_request("GET", "/lol-perks/v1/pages")
    pages = pages.json()

    if len(pages) == 0:
        #create page function
        print("Create page")
        lcu_request("POST", "/lol-perks/v1/pages/", runes)
    else:
        #update page
        currentPage = lcu_request("GET", "/lol-perks/v1/currentpage")
        currentPage = currentPage.json()
        lcu_request("PUT", "/lol-perks/v1/pages/" + str(currentPage["id"]), runes)