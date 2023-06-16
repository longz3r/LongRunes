import os

def startup():
    print("Starting Up")
    if not os.path.exists("C:/LongDev"):
        os.mkdir("C:/LongDev")
    if not os.path.exists("C:/LongDev/LongRunes"):
        os.mkdir("C:/LongDev/LongRunes")
    if not os.path.exists("C:/LongDev/LongRunes/lockfile"):
        createFile = open("C:/LongDev/LongRunes/lockfile", 'w')
        createFile.close()