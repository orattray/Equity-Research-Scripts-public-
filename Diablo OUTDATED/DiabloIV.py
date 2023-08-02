from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

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

# Print the live viewer figure
print("Live Viewer Figure for Diablo IV:", viewer_figure)

# Quit the WebDriver
driver.quit()
