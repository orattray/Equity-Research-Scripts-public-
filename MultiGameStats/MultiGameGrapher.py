import csv
import matplotlib.pyplot as plt
from pathlib import Path

script_directory = Path(__file__).parent.absolute()
relative_path = Path("Multigameapi.csv")
absolute_path = script_directory / relative_path

# Define the CSV file path
csv_file = absolute_path

# Read the data from the CSV file
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

# Create the line graphs
plt.figure()
plt.subplot(2, 1, 1)
plt.title('7-Day Viewer Figures')
plt.xlabel('Date')
plt.ylabel('Figure')
for game_name, data in viewer_figures.items():
    x = [row[0] for row in data]
    y = [row[1] for row in data]
    plt.plot(x, y, label=game_name)
plt.legend()

plt.subplot(2, 1, 2)
plt.title('Hours Watched')
plt.xlabel('Date')
plt.ylabel('Figure')
for game_name, data in hours_figures.items():
    x = [row[0] for row in data]
    y = [row[1] for row in data]
    plt.plot(x, y, label=game_name)
plt.legend()

plt.show()