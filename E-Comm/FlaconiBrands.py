import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Set the path to the ChromeDriver executable
chrome_driver_path = "C:\\Users\\OscarRattray\\Python scripts\\chromedriver\\chromedriver.exe"

# Set up ChromeDriver
service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run ChromeDriver in headless mode
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Create WebDriver instance
driver = webdriver.Chrome(service=service, options=options)

# Open the website
url = "https://www.flaconi.de/marken/"
driver.get(url)

# Wait for the page to load
time.sleep(10)  # Delay for 10 seconds

# Find all <a> elements that contain the brand names
brand_elements = driver.find_elements(By.CSS_SELECTOR, "a[href^='/']")

# Extract the brand names from the <a> elements
brand_names = [element.text for element in brand_elements]

# Count and print the number of brand names
brand_count = len(brand_names)
print(f"Total number of brand names: {brand_count}")

# Print all the brand names
for brand_name in brand_names:
    print(brand_name)

# Close the browser
driver.quit()
