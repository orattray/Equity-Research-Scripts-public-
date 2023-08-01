import csv
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
from pathlib import Path

script_directory = Path(__file__).parent.absolute()
relative_path = Path("Multigamest.csv")
absolute_path = script_directory / relative_path


# Path to the chromedriver executable
driver_path = '/opt/homebrew/bin/chromedriver'

# URLs of the websites and their corresponding game names
websites = {
    'https://twitchtracker.com/games/515024': 'Diablo IV',
    'https://twitchtracker.com/games/32982': 'GTA V',
    'https://twitchtracker.com/games/21779': 'League of Legends',
    'https://twitchtracker.com/games/516575': 'Valorant',
    'https://twitchtracker.com/games/2090279789': 'Final Fantasy XVI',
    'https://twitchtracker.com/games/493057': 'PUBG: BATTLEGROUNDS',
    'https://twitchtracker.com/games/33214': 'Fortnite',
    'https://twitchtracker.com/games/27471': 'Minecraft'
}

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run Chrome in headless mode

# Start the WebDriver
driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)

# Initialize a dictionary to store the average 7-day viewer figures
viewer_figures = {}

for url, game_name in websites.items():
    # Navigate to the website
    driver.get(url)

    # Find the div element with class "g-x-s-label" containing the label "Avg. viewers, 7 days"
    div_element = driver.find_element(By.XPATH, '//div[@class="g-x-s-label color-viewers" and text()="Avg. viewers, 7 days"]')

    # Find the parent div of the div containing the value
    parent_div = div_element.find_element(By.XPATH, '..')

    # Find the div element with class "g-x-s-value" inside the parent div
    value_element = parent_div.find_element(By.CLASS_NAME, 'g-x-s-value')

    # Extract the average 7-day viewer figure
    viewer_figure = value_element.text.strip().replace(',', '')  # Remove commas from the number

    # Store the viewer figure in the dictionary
    viewer_figures[game_name] = viewer_figure

# Get the current date and time
current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Define the CSV file path
csv_file = absolute_path

# Get the absolute file path
absolute_file_path = os.path.abspath(csv_file)

# Check if the CSV file already exists
csv_file_exists = os.path.exists(csv_file)

# Write the data to the CSV file
with open(csv_file, 'a', newline='') as file:
    writer = csv.writer(file)

    # Write the game names on the top line
    if not csv_file_exists or os.path.getsize(csv_file) == 0:
        writer.writerow(['Date and Time'] + list(websites.values()))

    # Write the data row
    writer.writerow([current_datetime] + list(viewer_figures.values()))

# Print the confirmation and absolute file path
print("Average 7-day Viewer Figures:")
for game_name, viewer_figure in viewer_figures.items():
    print(game_name + ":", viewer_figure)
print("Data appended to", absolute_file_path)

# Quit the WebDriver
driver.quit()
