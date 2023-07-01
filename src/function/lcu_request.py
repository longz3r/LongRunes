import requests
import urllib3
urllib3.disable_warnings()
from function.getLCUdata import port, authToken

# Make an HTTPS GET request
def lcu_request(endpoint):
    headers = {
    'Authorization': f'Basic {authToken}'
    }
    response = requests.get(f'https://127.0.0.1:{port}/{endpoint}', headers=headers, verify=False)



    # Check the response status code
    if response.status_code == 200:
        # Print the response content
        return response.text
    else:
        print('LCU request faied with status code:', response.status_code)
        print("Make sure League Client is running")
        return False
