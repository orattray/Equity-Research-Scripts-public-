import csv
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os

# Path to the chromedriver executable
driver_path = '/opt/homebrew/bin/chromedriver'

# URL of the website
url = 'https://twitchtracker.com/games/515024'

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run Chrome in headless mode

# Start the WebDriver
driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)

# Navigate to the website
driver.get(url)

# Find the div element with class "g-x-s-value"
div_element = driver.find_element(By.CLASS_NAME, 'g-x-s-value')

# Extract the live viewer figure
viewer_figure = div_element.text.strip()

# Get the current date and time
current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Create a dictionary with the data to be saved
data = {'Date and Time': current_datetime, 'Live Viewers': viewer_figure}

# Define the CSV file path
csv_file = '/Users/oscarrattray/Documents/LocalCode/Arete/Equity-Research-Scripts/Diablo/diablo_iv_live_viewers.csv'

# Get the absolute file path
absolute_file_path = os.path.abspath(csv_file)

# Write the data to the CSV file
try:
    with open(csv_file, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(data)
except Exception as e:
    print("Error occurred while writing to the CSV file:", str(e))

# Print the confirmation and absolute file path
print("Live Viewer Figure for Diablo IV:", viewer_figure)
print("Data appended to", absolute_file_path)

# Quit the WebDriver
driver.quit()
