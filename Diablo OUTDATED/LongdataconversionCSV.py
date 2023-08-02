import csv
import datetime
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

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

# Wait for the graph to load (adjust sleep time if necessary)
time.sleep(5)

# Find the x and y data points of the graph
x_elements = driver.find_elements(By.CSS_SELECTOR, 'g.highcharts-xaxis-labels text')
y_elements = driver.find_elements(By.CSS_SELECTOR, 'g.highcharts-series path')

# Extract x and y values from the elements
x_values = [element.text for element in x_elements]
y_values = [element.get_attribute('d') for element in y_elements]

# Process y values to extract the relevant data
data = []
for y_value in y_values:
    # Parse the path data to extract the y value
    y_data = y_value.split('L')[1:]  # Ignore the initial 'M' command
    
    # Convert the y data to numeric values
    y_data = [float(y.split(',')[1]) for y in y_data if len(y.split(',')) > 1]
    
    # Calculate the average y value (you can customize this based on your requirements)
    average_y = sum(y_data) / len(y_data) if y_data else 0
    
    # Append the data point to the list
    data.append(average_y)

# Get the current date and time
current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Create a dictionary with the data to be saved
data_dict = {'Date and Time': current_datetime, 'Graph Data': data}

# Define the CSV file path
csv_file = '/Users/oscarrattray/Documents/LocalCode/Arete/Equity-Research-Scripts/Diablo/output.csv'

# Write the data to the CSV file
try:
    with open(csv_file, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data_dict.keys())
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(data_dict)
except Exception as e:
    print("Error occurred while writing to the CSV file:", str(e))

# Print the confirmation
print("Data appended to", csv_file)

# Quit the WebDriver
driver.quit()
