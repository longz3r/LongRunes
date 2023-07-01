import startup
import asyncio

from function.test import mainTask

def main():
    print("Starting LongRunes...")
    startup()
    asyncio.run(mainTask())


if __name__ == "__main__":
    main()