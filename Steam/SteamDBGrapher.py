import csv
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from pathlib import Path

# Use Seaborn's default style for better visuals
sns.set_style("whitegrid")

script_directory = Path(__file__).parent.absolute()
relative_path = Path("steamdbmostplayed.csv")
absolute_path = script_directory / relative_path

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

fig, ax = plt.subplots(figsize=(10, 8))
for game_name, data in game_data.items():
    ax.plot(data['dates'], data['peak_players'], label=game_name)

ax.set_title('Peak Players on Steam')
ax.set_xlabel('Date')
ax.set_ylabel('Peak Players (last 24 hrs)')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
