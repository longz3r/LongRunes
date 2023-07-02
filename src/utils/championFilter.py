import requests
import json

def championFilter(version:str, language:str="en_US"):
    # Make a GET request to the JSON API
    response = requests.get(f'https://ddragon.leagueoflegends.com/cdn/{version}/data/{language}/champion.json')

    # Parse the response as JSON
    data = json.loads(response.text)

    # Define a function to filter the data
    def filter_data(data):
        filtered_data = {
            "version": version
        }
        for key, value in data['data'].items():
            filtered_champion = {
                "key": value["key"],
                "name": value["name"]#.replace(" ", "")
            }
            filtered_data[value["key"]] = filtered_champion["name"]#.lower()
        return filtered_data

    # Call the filter_data function and write the result to a file
    filtered_data = filter_data(data)
    with open('C:/LongDev/LongRunes/champion.json', 'w') as f:
        json.dump(filtered_data, f, indent=2)
