import csv
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path

script_directory = Path(__file__).parent.absolute()
relative_path = Path("youtubetopgames.csv")
absolute_path = script_directory / relative_path


# URL of the YouTube page with the games
url = 'https://www.youtube.com/gaming/games'

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run Chrome in headless mode

# Start the WebDriver
driver = webdriver.Remote(command_executor='http://localhost:9515', options=chrome_options)

# Navigate to the YouTube page with the games
driver.get(url)

# Wait for the cookie consent pop-up to appear
wait = WebDriverWait(driver, 10)
cookie_consent = wait.until(EC.visibility_of_element_located((By.ID, 'yDmH0d')))

# Find the "Accept all" button by its text content
accept_button = cookie_consent.find_element(By.XPATH, '//button[contains(.,"Accept all")]')

# Click the "Accept all" button
accept_button.click()

# Wait for the games to load (adjust the sleep duration if necessary)
driver.implicitly_wait(5)

# Find the game and viewer figure elements on the page
game_viewer_pairs = driver.find_elements(By.CSS_SELECTOR, 'ytd-game-details-renderer')
game_names = []
viewer_figures = []

# Iterate over the game and viewer pairs to retrieve the data
for pair in game_viewer_pairs[:16]:
    game_element = pair.find_element(By.CSS_SELECTOR, '#title')
    viewer_element = pair.find_element(By.CSS_SELECTOR, '#live-viewers-count')
    game_name = game_element.text.strip()
    viewer_figure = viewer_element.text.strip().split()[0]
    game_names.append(game_name)
    viewer_figures.append(viewer_figure)

# Quit the WebDriver
driver.quit()

# Combine game names and viewer figures into a dictionary
game_data = dict(zip(game_names, viewer_figures))

# Define the CSV file path
csv_file = absolute_path

# Get the current date and time
current_datetime = datetime.datetime.now().strftime('%Y-%m-%d')

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
