import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

script_directory = Path(__file__).parent.absolute()
relative_path = Path("youtubetopgames.csv")
absolute_path = script_directory / relative_path

# Load the CSV file and parse the DateTime column as a datetime object
df = pd.read_csv(absolute_path, parse_dates=['DateTime'])

# Convert viewer figures to integers
df['Viewer Figure'] = df['Viewer Figure'].str.replace('K', '000').str.replace('.', '').astype(int)

# Group by game and plot a line graph for each game
fig, ax = plt.subplots()
for game, data in df.groupby('Game'):
    ax.plot(data['DateTime'], data['Viewer Figure'], label=game)

# Add labels and legend
plt.xlabel('Time')
plt.ylabel('Viewers')
plt.legend()

# Show the plot
plt.show()