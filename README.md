
---

# Python Scripts for Game Data Retrieval and Visualization

This repository contains a collection of Python scripts to retrieve data related to games from various sources and visualize it through charts. These scripts are useful for monitoring game popularity, viewer figures, and peak player counts.

# Automated Scripts


## Automated Data Grab (AUTOMATEDGrabData.py)

### Description
This Python script automates the process of grabbing data from a website. It uses the ChromeDriver executable to open a Chrome browser window and then runs a separate Python script to scrape the data. Once the data has been collected, the ChromeDriver executable is closed.

To use this script, make sure you have the ChromeDriver executable and the "grab all data" Python file in the correct directories. Then, simply run the script and wait for it to finish.

### Requirements
- Python
- Selenium
- ChromeDriver executable
- Python scripts to scrape data

### Usage
1. Ensure you have Python installed.
2. Install required packages by running setup.bat
3. Place the correct ChromeDriver executable in the chromedriver folder.

## Generate all graphs (Generate all graphs.py)

### Description

This Python script generates graphs for various games and platforms using separate Python scripts for each. The script uses the subprocess module to run each script in a separate thread, allowing for parallel execution. The generated graphs are saved in a folder called "Graphs" in the same directory as the script.

To use this script, make sure you have all the necessary Python scripts in the correct directories. Then, simply run the script and wait for it to finish. The generated graphs will be saved in the "Graphs" folder.

### Requirements
- Python
- subprocess
- Python scripts to generate graphs

### Usage
1. Ensure you have Python installed.
2. Install required packages by running setup.bat



# Manual Scripts

## 1. Twitch Game Viewer Figures (MultiGameAPIEA.py)

### Description
This script retrieves average 7-day viewer figures and hours watched for several EA games using TwitchTracker's API. It saves the data to a CSV file and creates line graphs to visualize the viewer figures and hours watched over time.

### Requirements
- Python
- requests
- json
- csv
- datetime
- plotly

### Usage
1. Ensure you have Python installed.
2. Install required packages using pip:
   ```
   pip install requests
   pip install plotly
   ```
3. Execute the script to retrieve data and generate viewer figures and hours watched charts:
   ```
   python EAMultiGame.py
   ```

## 2. YouTube Games Viewer Figures (youtubegamesscraperv2.py)

### Description
This script scrapes the viewer figures of top games from the YouTube gaming page using Selenium WebDriver. It appends the data to a CSV file with a timestamp for each execution.

### Requirements
- Python
- Selenium
- csv
- datetime

### Usage
1. Ensure you have Python installed.
2. Install required packages using pip:
   ```
   pip install selenium
   ```
3. Execute the script to obtain the viewer figures and update the CSV file:
   ```
   python youtube_viewer_figures.py
   ```

## 3. SteamDB Most Played Games (steamdbscraperv1.py)

### Description
This script navigates to SteamDB and retrieves the most played games along with their peak player counts. It appends the data to a CSV file with a timestamp for each execution.

### Requirements
- Python
- Selenium
- csv
- datetime

### Usage
1. Ensure you have Python installed.
2. Install required packages using pip:
   ```
   pip install selenium
   ```
3. Execute the script to fetch the most played games and update the CSV file:
   ```
   python steamdb_most_played.py
   ```

## 4. Twitch Game Viewer Figures and Charts (EATwitchwGraphs.py)

### Description
This script fetches average 7-day viewer figures and hours watched for EA games from TwitchTracker's API, saves the data to a CSV file, and creates line charts to visualize the data over time.

### Requirements
- Python
- requests
- json
- csv
- datetime
- plotly

### Usage
1. Ensure you have Python installed.
2. Install required packages using pip:
   ```
   pip install requests
   pip install plotly
   ```
3. Execute the script to get the data, generate viewer figures and hours watched charts, and save them as HTML files:
   ```
   python EAGameCharts.py
   ```

## 5. SteamDB Peak Players Line Chart (steamdbgrapher.py)

### Description
This script reads peak player count data from a CSV file and creates a line chart using Matplotlib to visualize the peak players on Steam for each game over time.

### Requirements
- Python
- csv
- matplotlib
- datetime

### Usage
1. Ensure you have Python installed.
2. Install required packages using pip:
   ```
   pip install matplotlib
   ```
3. Execute the script to read the data and plot the line chart:
   ```
   python steamdb_peak_players.py
   ```

---

Please note that these scripts are provided as-is and may require adjustments to file paths and driver installations based on your system's configuration.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---