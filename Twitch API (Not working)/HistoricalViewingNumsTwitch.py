import requests

# Twitch API endpoint for getting historical game data
GAME_ANALYTICS_ENDPOINT = "https://api.twitch.tv/helix/analytics/games"

# Your OAuth token and client ID
OAUTH_TOKEN = "your_oauth_token_here"
CLIENT_ID = "your_client_id_here"

# Specify the game ID and date range
GAME_ID = "33214"
START_DATE = "2020-01-01T00:00:00Z"
END_DATE = "2021-03-01T00:00:00Z"

# Set up the headers with authentication and required headers
headers = {
    "Client-ID": CLIENT_ID,
    "Authorization": f"Bearer {OAUTH_TOKEN}",
}

# Set up the parameters for the API request
params = {
    "game_id": GAME_ID,
    "started_at": START_DATE,
    "ended_at": END_DATE,
}

# Make the API request
response = requests.get(GAME_ANALYTICS_ENDPOINT, headers=headers, params=params)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()
    # Process the data as per your requirements
    # ...
else:
    print(f"Error: {response.status_code} - {response.text}")
