import os
from function.getAuthorization import getAuthorization

def startup():
    print("Starting Up")
    if not os.path.exists("C:/LongDev"):
        os.mkdir("C:/LongDev")
    if not os.path.exists("C:/LongDev/LongRunes"):
        os.mkdir("C:/LongDev/LongRunes")
    getAuthorization()