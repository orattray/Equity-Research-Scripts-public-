import requests

# Twitch API endpoint for obtaining OAuth tokens
TOKEN_URL = "https://id.twitch.tv/oauth2/token"

# Your client ID and client secret
CLIENT_ID = "your_client_id_here"
CLIENT_SECRET = "your_client_secret_here"

# The list of scopes your application requires (separated by spaces)
SCOPES = "analytics:read:extensions"

def get_oauth_token():
    # Set up the parameters for the token request
    params = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "client_credentials",
        "scope": SCOPES,
    }

    # Make the token request
    response = requests.post(TOKEN_URL, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        return data["access_token"]
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Call the function to get the OAuth token
oauth_token = get_oauth_token()

if oauth_token:
    print(f"OAuth token: {oauth_token}")
    # Use the token for your API requests
    # ...
