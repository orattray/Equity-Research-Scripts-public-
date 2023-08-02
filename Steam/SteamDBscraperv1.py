import csv
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path

script_directory = Path(__file__).parent.absolute()
relative_path = Path("steamdbmostplayed.csv")
absolute_path = script_directory / relative_path


# Create an instance of the webdriver class in headless mode with disabled web security
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

# Navigate to the SteamDB website
driver.get('https://steamdb.info')

# Wait for the table to load
wait = WebDriverWait(driver, 10)
table_div = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.span6')))
table = table_div.find_element(By.CSS_SELECTOR, 'table.table-products')

# Find the rows in the table and extract the game names and peak player counts
rows = table.find_elements(By.TAG_NAME, 'tr')
game_names = []
peak_players = []
for row in rows[2:17]:
    game_element = row.find_element(By.CSS_SELECTOR, 'td:nth-child(2) > a.css-truncate')
    player_element = row.find_element(By.CSS_SELECTOR, 'td.text-center.green')
    game_name = game_element.text.strip()
    peak_player_count = player_element.text.strip().replace(',', '')
    if peak_player_count:
        peak_players.append(int(peak_player_count))
    else:
        peak_players.append(0)
    game_names.append(game_name)

# Get the current date and time
current_datetime = datetime.datetime.now().strftime('%Y-%m-%d')

# Combine game names and peak player counts into a dictionary
game_data = dict(zip(game_names, peak_players))

# Write the data to the CSV file (append mode)
csv_file = absolute_path
with open(csv_file, 'a', newline='') as file:
    writer = csv.writer(file)

    # Check if the file is empty (no header present)
    is_file_empty = file.tell() == 0

    # Write the header if the file is empty
    if is_file_empty:
        writer.writerow(['Date', 'Game', 'Peak Players 24hr'])

    # Write the data rows
    for game, viewers in game_data.items():
        writer.writerow([current_datetime, game, viewers])

    # Write an empty row
    writer.writerow([])

# Print a message indicating where the output was saved
print(f'Output appended to {csv_file}')