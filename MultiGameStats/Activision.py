import csv
import datetime
import requests
import os
import json
import time
from pathlib import Path

print("Waiting for 5 seconds...")
time.sleep(5)  # Wait for 5 seconds before continuing


script_directory = Path(__file__).parent.absolute()
relative_path = Path("ActivisionData.csv")
absolute_path = script_directory / relative_path


# URLs of the games' API endpoints
api_endpoints = {
    'Call of Duty: Modern Warfare II': 'https://twitchtracker.com/api/games/summary/1678052513',
    'Call of Duty: Warzone': 'https://twitchtracker.com/api/games/summary/512710',
    'Overwatch 2': 'https://twitchtracker.com/api/games/summary/515025',
    'Diablo IV': 'https://twitchtracker.com/api/games/summary/515024',
    'World of Warcraft': 'https://twitchtracker.com/api/games/summary/18122'
}

# Initialize a dictionary to store the average 7-day viewer figures
viewer_figures = {}
hours_figures = {}

for game_name, api_endpoint in api_endpoints.items():
    attempts = 0
    while attempts < 3:
        # Make a GET request to the API endpoint
        response = requests.get(api_endpoint)

        # Check if the response is empty
        if not response.content:
            print(f"Error: Empty response from {api_endpoint}")
            attempts += 1
            time.sleep(1)  # Wait for 1 second before retrying
            continue

        # Parse the JSON response
        try:
            data = response.json()
            break
        except json.JSONDecodeError as e:
            print(f"Error: Failed to parse JSON response from {api_endpoint}: {e}")
            attempts += 1
            time.sleep(1)  # Wait for 1 second before retrying
            continue

    # Extract the average 7-day viewer figure
    viewer_figure = str(data['avg_viewers'])
    hours_figure = str(data['hours_watched'])

    # Store the viewer figure in the dictionary
    viewer_figures[game_name] = viewer_figure
    hours_figures[game_name] = hours_figure

# Get the current date and time
current_datetime = datetime.datetime.now().strftime('%Y-%m-%d')
File_datetime = datetime.datetime.now().strftime('%Y-%m-%d')

# Define the CSV file path
csv_file = absolute_path

# Check if the CSV file exists and is not empty
csv_file_exists = os.path.exists(csv_file)
if csv_file_exists and os.path.getsize(csv_file) == 0:
    csv_file_exists = False

# Write the data to the CSV file
with open(csv_file, mode='a', newline='') as csv_file:
    writer = csv.writer(csv_file)

    # Write the header row if the CSV file is empty
    if not csv_file_exists:
        writer.writerow(['Game', 'Average 7-Day Viewers', 'Hours Watched', 'Date'])

    # Write the data rows
    for game_name, viewer_figure in viewer_figures.items():
        hours_figure = hours_figures[game_name]
        writer.writerow([game_name, viewer_figure, hours_figure, current_datetime])

# Print the confirmation and relative file path
print("Average 7-day Viewer Figures:")
for game_name, viewer_figure in viewer_figures.items():
    print(game_name + ":", viewer_figure)
print("Hours Watched:")
for game_name, hours_figure in hours_figures.items():
    print(game_name + ":", hours_figure)    
print("Data appended to", csv_file)