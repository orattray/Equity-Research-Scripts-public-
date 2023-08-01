import csv
import datetime
import requests
import os
import json
import matplotlib.pyplot as plt
from pathlib import Path

script_directory = Path(__file__).parent.absolute()
relative_path = Path("EAMultiGame.csv")
absolute_path = script_directory / relative_path


# URLs of the games' API endpoints
api_endpoints = {
    'FIFA 23': 'https://twitchtracker.com/api/games/summary/1745202732',
    'Madden NFL 23': 'https://twitchtracker.com/api/games/summary/862021340',
    'Battlefield 2042': 'https://twitchtracker.com/api/games/summary/514974',
    'NHL 23': 'https://twitchtracker.com/api/games/summary/731327454',
    'F1 23': 'https://twitchtracker.com/api/games/summary/174553474',
    'Star Wars Jedi: Survivor': 'https://twitchtracker.com/api/games/summary/1407096487',
    'The Sims 4': 'https://twitchtracker.com/api/games/summary/369252',
    'Apex Legends': 'https://twitchtracker.com/api/games/summary/511224'
}

# Initialize a dictionary to store the average 7-day viewer figures
viewer_figures = {}
hours_figures = {}

for game_name, api_endpoint in api_endpoints.items():
    # Make a GET request to the API endpoint
    response = requests.get(api_endpoint)

    # Check if the response is empty
    if not response.content:
        print(f"Error: Empty response from {api_endpoint}")
        continue

    # Parse the JSON response
    try:
        data = response.json()
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse JSON response from {api_endpoint}: {e}")
        continue

    # Extract the average 7-day viewer figure
    viewer_figure = str(data['avg_viewers'])
    hours_figure = str(data['hours_watched'])

    # Store the viewer figure in the dictionary
    viewer_figures[game_name] = viewer_figure
    hours_figures[game_name] = hours_figure

# Get the current date and time
current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
File_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H_%M_%S')

# Define the CSV file path
csv_file = absolute_path

# Check if the CSV file exists and is not empty
csv_file_exists = os.path.exists(csv_file)
if csv_file_exists and os.path.getsize(csv_file) == 0:
    csv_file_exists = False

# Check if the CSV file exists and is not empty
csv_file_exists = os.path.exists(csv_file)
if csv_file_exists and os.path.getsize(csv_file) == 0:
    csv_file_exists = False

# Write the data to the CSV file
with open(csv_file, mode='a', newline='') as csv_file_obj:
    writer = csv.writer(csv_file_obj)

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

# Read the data from the CSV file
data = []
with open(csv_file, mode='r') as csv_file_obj:
    reader = csv.DictReader(csv_file_obj)
    for row in reader:
        data.append(row)

# Create the charts folder if it doesn't exist
if not os.path.exists('charts'):
    os.makedirs('charts')

# Create a list of game names and viewer figures
game_names = [row['Game'] for row in data]
viewer_figures = [int(row['Average 7-Day Viewers']) for row in data]

# Create a bar chart of the viewer figures
fig, ax = plt.subplots()
ax.bar(game_names, viewer_figures)

# Set the chart title and axis labels
ax.set_title('Average 7-Day Viewers for EA Games')
ax.set_xlabel('Game')
ax.set_ylabel('Viewers')

# Save the chart as a PNG image in the charts folder
plt.savefig('charts/{}.png'.format(File_datetime))

# Display the chart in the IDE
plt.show()