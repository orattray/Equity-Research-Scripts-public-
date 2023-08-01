import csv
import datetime
import requests
import os
import json
import plotly.graph_objs as go
import plotly.io as pio
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

# Create a list of game names and viewer figures
game_names = [row['Game'] for row in data]
viewer_figures = {game_name: [] for game_name in set(game_names)}
hours_figures = {game_name: [] for game_name in set(game_names)}
dates = []

for row in data:
    game_name = row['Game']
    viewer_figure = int(row['Average 7-Day Viewers'])
    hours_figure = int(row['Hours Watched'])
    date = row['Date']
    viewer_figures[game_name].append(viewer_figure)
    hours_figures[game_name].append(hours_figure)
    dates.append(date)

# Create a line graph of the viewer figures over time
viewer_figures_fig = go.Figure()
for game_name in set(game_names):
    viewer_figures_fig.add_trace(go.Scatter(x=dates, y=viewer_figures[game_name], name=game_name))

# Set the chart title and axis labels
viewer_figures_fig.update_layout(title='Average 7-Day Viewers for EA Games', xaxis_title='Date', yaxis_title='Viewers')

# Save the chart to an HTML file
viewer_figures_html_file_path = fr'{File_datetime} 7Dayviewers.html'
pio.write_html(viewer_figures_fig, file=viewer_figures_html_file_path, auto_open=True)

# Create a line graph of the hours watched over time
hours_figures_fig = go.Figure()
for game_name in set(game_names):
    hours_figures_fig.add_trace(go.Scatter(x=dates, y=hours_figures[game_name], name=game_name))

# Set the chart title and axis labels
hours_figures_fig.update_layout(title='Hours Watched for EA Games', xaxis_title='Date', yaxis_title='Hours')

# Save the chart to an HTML file
hours_figures_html_file_path = fr'{File_datetime} HoursWatched.html'
pio.write_html(hours_figures_fig, file=hours_figures_html_file_path, auto_open=True)

# Print the confirmation
print("Charts saved to HTML files")