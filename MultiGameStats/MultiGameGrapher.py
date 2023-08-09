import csv
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Use Seaborn's default style for better visuals
sns.set_style("whitegrid")

script_directory = Path(__file__).parent.absolute()
relative_path = Path("Multigameapi.csv")
absolute_path = script_directory / relative_path

csv_file = absolute_path

viewer_figures = {}
hours_figures = {}
with open(csv_file, mode='r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        game_name = row['Game']
        viewer_figure = float(row['Average 7-Day Viewers'])
        hours_figure = float(row['Hours Watched'])
        date = row['Date']
        if game_name not in viewer_figures:
            viewer_figures[game_name] = []
        if game_name not in hours_figures:
            hours_figures[game_name] = []
        viewer_figures[game_name].append((date, viewer_figure))
        hours_figures[game_name].append((date, hours_figure))

plt.figure(figsize=(10, 8))

plt.subplot(2, 1, 1)
plt.title('Average Viewers over the Past 7 Days')
plt.xlabel('Date')
plt.ylabel('Average Viewers')
for game_name, data in viewer_figures.items():
    x = [row[0] for row in data]
    y = [row[1] for row in data]
    plt.plot(x, y, label=game_name)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.xticks(rotation=45)

plt.subplot(2, 1, 2)
plt.title('Total Hours Watched')
plt.xlabel('Date')
plt.ylabel('Hours')
for game_name, data in hours_figures.items():
    x = [row[0] for row in data]
    y = [row[1] for row in data]
    plt.plot(x, y, label=game_name)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
