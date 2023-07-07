import asyncio
from function.lcu_request import lcu_request
from function.applyRune import applyRune

# Store the previous data received from the HTTP endpoint
previous_data = None

async def getCurrentChampion():
    global previous_data

    # Make an HTTP request to fetch the data from the endpoint
    response = lcu_request("GET", "/lol-champ-select/v1/current-champion")
    # Process the response
    if response != False:
        # Compare the data with the previous response
        if response != previous_data:
            # print("Data has changed:", response)
            previous_data = response
            if response != "0" and response != None:
                applyRune(response)

    # Schedule the next HTTP request after 5 seconds
    await asyncio.sleep(2)
    await getCurrentChampion()

async def asyncTask():
    # Start the HTTP request task
    http_task = asyncio.create_task(getCurrentChampion())

    # Start the WebSocket client task

    # Run the tasks concurrently
    await asyncio.gather(http_task)
