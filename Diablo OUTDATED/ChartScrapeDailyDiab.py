import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if __name__ == "__main__":
    # Path to the chromedriver executable
    driver_path = '/opt/homebrew/bin/chromedriver'

    # URL of the website
    url = 'https://twitchtracker.com/games/515024'

    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run Chrome in headless mode

    # Start the WebDriver
    driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)

    # Call URL through selenium driver
    driver.get(url)

    # Wait until element with highcharts graph appears
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "highcharts-series-group"))
    )

    # Parse dates and values in those dates
    dates = driver.execute_script('return Highcharts.charts[0].series[0].xData.map(x => new Date(x).toISOString())')
    values = driver.execute_script('return Highcharts.charts[0].series[0].yData')

    # Create a list of dictionaries for each data point
    data = [{'Dates': date, 'Viewers': value} for date, value in zip(dates, values)]

    # Append data to the CSV file
    csv_file = 'output.csv'
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Dates', 'Viewers'])
        writer.writerows(data)

    # Quit the driver
    driver.quit()
