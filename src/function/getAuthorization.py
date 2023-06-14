import subprocess
import re
from base64encode import encodeToken

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
    print(port.split("=")[1])
    print(encodeToken(authToken.split("=")[1]))
