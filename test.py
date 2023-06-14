import requests
import urllib3
urllib3.disable_warnings()
fuas = 123
def ngu():
    print(fuas)

# Make an HTTPS GET request
headers = {
    'Authorization': 'Basic cmlvdDoxYnYtTHJKdkZDYmtNd08xZ0ctR2JB'
}
response = requests.get('https://127.0.0.1:57121/lol-summoner/v1/current-summoner', headers=headers, verify=False)



# Check the response status code
if response.status_code == 200:
    # Print the response content
    print(response.text)
else:
    print('Request faied with status code:', response.status_code)
    print(response.text)
