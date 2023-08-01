import csv
import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pathlib import Path

script_directory = Path(__file__).parent.absolute()
relative_path = Path("youtubetopgames.csv")
absolute_path = script_directory / relative_path

# Define the URL of the web page to scrape
url = 'https://www.youtube.com/gaming/games'

# Define the options for the Chrome driver
options = webdriver.ChromeOptions()

# Connect to the existing Chrome driver instance
driver = webdriver.Remote(command_executor='http://localhost:9515', options=options)

# Navigate to the web page
driver.get(url)

# Wait for the accept button to appear and click it
accept_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Accept all"]')))
accept_button.click()

# Wait for the page to load
driver.implicitly_wait(10)

# Find the top games section
top_games_section = driver.execute_script('return document.querySelector("#contents ytd-grid-renderer")')

# Find the game names and viewer figures
game_names = [game_name.text for game_name in top_games_section.find_elements_by_xpath('.//div[@id="meta"]/div[@id="title"]')]
viewer_figures = []
for viewer_figure_element in top_games_section.find_elements_by_xpath('.//div[@id="meta"]/div[@id="subtitle"]'):
    viewer_figure_text = viewer_figure_element.text
    if viewer_figure_text.endswith('K'):
        viewer_figure = int(float(viewer_figure_text[:-1]) * 1000)
    else:
        viewer_figure = int(viewer_figure_text)
    viewer_figures.append(viewer_figure)

# Quit the WebDriver
driver.quit()

# Combine game names and viewer figures into a dictionary
game_data = dict(zip(game_names, viewer_figures))

# Define the CSV file path
csv_file = absolute_path

# Get the current date and time
current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Write the data to the CSV file (append mode)
with open(csv_file, 'a', newline='') as file:
    writer = csv.writer(file)

    # Check if the file is empty (no header present)
    is_file_empty = file.tell() == 0

    # Write the header if the file is empty
    if is_file_empty:
        writer.writerow(['DateTime', 'Game', 'Viewer Figure'])

    # Write the data rows
    for game, viewers in game_data.items():
        writer.writerow([current_datetime, game, viewers])

    # Write an empty row
    writer.writerow([])

# Print the confirmation
print("Data written to", csv_file)