# import startup
import asyncio

from asyncTask import asyncTask
from function.getCurrentSummoner import getCurrentSummoner
from startup import startup

def main():
    print("Starting LongRunes...")
    startup()

    print("Welcome", getCurrentSummoner()["displayName"])
    asyncio.run(asyncTask())


if __name__ == "__main__":
    main()