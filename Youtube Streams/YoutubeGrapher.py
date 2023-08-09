import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Use Seaborn's default style for better visuals
sns.set_style("whitegrid")

script_directory = Path(__file__).parent.absolute()
relative_path = Path("youtubetopgames.csv")
absolute_path = script_directory / relative_path

# Load the CSV file and parse the DateTime column as a datetime object
df = pd.read_csv(absolute_path, parse_dates=['DateTime'])

# Convert viewer figures to integers
df['Viewer Figure'] = df['Viewer Figure'].str.replace('K', '000').str.replace('.', '').astype(int)

fig, ax = plt.subplots(figsize=(10, 8))
for game, data in df.groupby('Game'):
    ax.plot(data['DateTime'], data['Viewer Figure'], label=game)

ax.set_xlabel('Time')
ax.set_ylabel('Viewers')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
