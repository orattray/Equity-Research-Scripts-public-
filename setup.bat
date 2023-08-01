#!/bin/bash

# Install required packages
echo "Installing required packages"
pip install requests beautifulsoup4 selenium pandas matplotlib requests plotly

# Install ChromeDriver
echo "Installing ChromeDriver (Macos only)"
# Install on macOS using Homebrew
if [[ "$OSTYPE" == "darwin"* ]]; then
    brew install chromedriver
    # Install on Windows using Chocolatey
elif [[ "$OSTYPE" == "msys"* ]]; then
    echo "On Windows manual download and install is required. See https://chromedriver.chromium.org/downloads"
fi

echo "Setup completed successfully!"

pause