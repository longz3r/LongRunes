import subprocess
import re
import os
from utils.base64encode import encodeToken

def getAuthorization():
    #chatgpt :))
    # Define the command to execute
    command = "wmic PROCESS WHERE name='LeagueClientUx.exe' GET commandline "  # Replace with your desired command
    # Run the command in the cmd and capture the output
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate()
    # Decode the output from bytes to string
    output = stdout.decode('utf-8')


    #check if the output is empty or not
    if output.strip() == "":
        print("League client not found")
    else:
        #search the output to find matched port and auth token
        port = re.search("--app-port=([0-9]*)", output).group()
        authToken = re.search("--remoting-auth-token=([\w-]*)", output).group()
        #split the output and take whatever behind the "="
        port = port.split("=")[1]
        authToken = encodeToken(authToken.split("=")[1])
        if os.path.exists("C:/LongDev/LongRunes/lcuData"):
            os.remove("C:/LongDev/LongRunes/lcuData")
        data = open("C:/LongDev/LongRunes/lcuData", "w+")
        data.write("DO NOT CHANGE OR DELETE THIS FILE WHEN LONGRUNES IS RUNNING\n")
        data.writelines([port + "\n", authToken + "\n"])

getAuthorization()