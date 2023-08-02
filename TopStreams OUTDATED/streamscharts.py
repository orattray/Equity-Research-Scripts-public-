import csv
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Path to ChromeDriver executable
driver_path = "/opt/homebrew/bin/chromedriver"

# URL of the website
url = "https://streamscharts.com/games"

# Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode

# Initialize ChromeDriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the website
driver.get(url)

# Find the top ten games
game_elements = driver.find_elements(By.CSS_SELECTOR, ".game-name")

# Get the current date and time
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Extract game names and viewer counts
games = []
for game_element in game_elements[:10]:
    game_name = game_element.text.strip()
    viewer_count = game_element.find_element(By.XPATH, "..//following-sibling::div[@class='viewer-count']").text.replace(",", "")
    games.append((game_name, viewer_count))

# Print the top ten games
for game in games:
    print(f"Game: {game[0]}, Viewer Count: {game[1]}")

# Append data to CSV file
csv_file = ""
with open(csv_file, mode="a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([current_datetime] + [game[0] for game in games])

# Close the browser
driver.quit()
