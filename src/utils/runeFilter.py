import requests
import json

# Make a GET request to the JSON API
def runeFilter(version:str, language:str="en_US"):
    response = requests.get(f'https://ddragon.leagueoflegends.com/cdn/{version}/data/{language}/runesReforged.json')

    # Parse the response as JSON
    data = json.loads(response.text)
    # Define a function to filter the data
    def filter_data(data):
        filtered_data = {
            "version": version,
            "statmodsattackspeedicon": 5005,
            "statmodsadaptiveforceicon": 5008,
            "statmodsarmoricon": 5002,
            "statmodsmagicresicon": 5003,
            "statmodshealthscalingicon": 5001,
            "statmodscdrscalingicon": 5007,
            #nimbus cloak fix
            "6361": 8275,
        }
        for item in data:
            filtered_data[item["key"]] = item["id"]
            for slot in item["slots"]:
                for rune in slot["runes"]:
                    if rune['key'].lower() == "lethaltempo":
                        rune['key'] = "lethaltempotemp"
                    if rune['key'].lower() == "tasteofblood":
                        rune['key'] = "greenterror_tasteofblood"
                    if rune['key'].lower() == "celerity":
                        rune['key'] = "celeritytemp"
                    filtered_data[rune['key'].lower()] = rune['id']
        return filtered_data


    # Call the filter_data function and write the result to a file
    filtered_data = filter_data(data)
    with open('C:/LongDev/LongRunes/runes.json', 'w') as f:
        json.dump(filtered_data, f, indent=2)
    print("done")