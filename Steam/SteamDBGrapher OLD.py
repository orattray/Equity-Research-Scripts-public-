import csv
import matplotlib.pyplot as plt
from datetime import datetime
from pathlib import Path

script_directory = Path(__file__).parent.absolute()
relative_path = Path("steamdbmostplayed.csv")
absolute_path = script_directory / relative_path


# Read the data from the CSV file
filename = absolute_path
game_data = {}
with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        game_name = row['Game']
        peak_players = int(row['Peak Players 24hr'])
        date_time_str = row['Date']
        date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d')
        if game_name not in game_data:
            game_data[game_name] = {'dates': [], 'peak_players': []}
        game_data[game_name]['dates'].append(date_time_obj)
        game_data[game_name]['peak_players'].append(peak_players)

# Plot a separate line for each game
fig, ax = plt.subplots()
for game_name, data in game_data.items():
    ax.plot(data['dates'], data['peak_players'], label=game_name)

# Set the title and axis labels
ax.set_title('Peak Players on Steam')
ax.set_xlabel('Date')
ax.set_ylabel('Peak Players (last 24 hrs)')

# Add a legend and show the plot
ax.legend()
plt.show()