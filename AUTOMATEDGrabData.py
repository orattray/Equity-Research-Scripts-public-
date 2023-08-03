import subprocess
import time
from pathlib import Path

script_directory = Path(__file__).parent.absolute()
relative_pathpy = Path("Grab all data.py")
absolute_pathpy = script_directory / relative_pathpy
relative_pathchrome = Path("chromedriver/chromedriver.exe")
absolute_pathchrome = script_directory / relative_pathchrome


# Set the path to the ChromeDriver executable
chromedriver_path = absolute_pathchrome

# Open the ChromeDriver executable
chrome_process = subprocess.Popen([chromedriver_path])

print("ChromeDriver started, script will run in 5 seconds, Please do not close this window it will autoclose when all scripts are done")
print ("For help please refer to the documentation on: https://github.com/orattray/Equity-Research-Scripts-public-")

# Wait for the ChromeDriver to start up
time.sleep(5)

# Set the path to the "grab all data" Python file
grab_all_data_path = absolute_pathpy

# Run the "grab all data" Python file
grab_process = subprocess.run(['python', grab_all_data_path], check=True)

# Close the ChromeDriver executable
chrome_process.kill()