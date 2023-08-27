import requests
import urllib3
urllib3.disable_warnings()
from function.getLCUdata import port, authToken

# Make an HTTPS GET request
def lcu_request(method:str, endpoint:str, data={}):
    headers = {
    'Authorization': f'Basic {authToken}'
    }
    if method == "GET":
        response = requests.get(f'https://127.0.0.1:{port}{endpoint}', headers=headers, verify=False)
        # Check the response status code
        if response.status_code == 200:
            # Print the response content
            return response.text
        else:
            if endpoint == "/lol-champ-select/v1/current-champion" and response.text == '{"errorCode":"RPC_ERROR","httpStatus":404,"implementationDetails":{},"message":"No active delegate"}':
                return
            else:
                print('LCU request faied with status code:', response.status_code)
                print("Error message:", response.text)
                print("Make sure League Client is running")
                return False
    elif method == "POST":
        response = requests.post(f'https://127.0.0.1:{port}{endpoint}', headers=headers, verify=False, data=data)
        # Check the response status code
        if response.status_code == 200:
            # Print the response content
            return response.text
        else:
            print('LCU request faied with status code:', response.status_code)
            print("Error message:", response.text)
            print("Make sure League Client is running")
            return False
    elif method == "PUT":
        response = requests.put(f'https://127.0.0.1:{port}{endpoint}', headers=headers, verify=False, json=data)
        # Check the response status code
        if response.status_code == 200 or (response.status_code == 201 and endpoint == "/lol-perks/v1/pages/"):
            # Print the response content
            return response.text
        # else:
        #     print('LCU request faied with status code:', response.status_code)
        #     print("Error message:", response.text)
        #     print("Make sure League Client is running")
        #     return False
