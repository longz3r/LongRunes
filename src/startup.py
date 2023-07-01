import os

def startup():
    if not os.path.exists("C:/LongDev"):
        os.mkdir("C:/LongDev")
    if not os.path.exists("C:/LongDev/LongRunes"):
        os.mkdir("C:/LongDev/LongRunes")