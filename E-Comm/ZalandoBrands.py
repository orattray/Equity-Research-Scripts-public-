from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Set the path to the ChromeDriver executable
chrome_driver_path = "C:\Users\OscarRattray\Python scripts\chromedriver\chromedriver.exe"

# Set up ChromeDriver
service = Service(chrome_driver_path)
options = Options()
options.headless = True
driver = webdriver.Chrome(service=service, options=options)

# Open the website
url = "https://en.zalando.de/brands/beauty/"
driver.get(url)

# Find all span elements with the specified class attribute
brand_elements = driver.find_elements(By.CSS_SELECTOR, "span.KxHAYs.lystZ1.FxZV-M._4F506m")

# Extract the brand names from the span elements
brand_names = [element.text for element in brand_elements]

# Count and print the number of brand names
brand_count = len(brand_names)
print(f"Total number of brand names: {brand_count}")

# Print all the brand names
for brand_name in brand_names:
    print(brand_name)

# Close the browser
driver.quit()
