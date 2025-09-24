import requests
import os
from dotenv import load_dotenv

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"

def get_access_token():
    response = requests.post(
        SPOTIFY_TOKEN_URL,
        data={"grant_type": "client_credentials"},
        auth=(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)
    )
    response.raise_for_status()
    return response.json()["access_token"]

def make_request(endpoint, method="GET", data=None):
    token = get_access_token()
    headers = {"Authorization": f"Bearer {token}"}
    
    if method == "GET":
        return requests.get(endpoint, headers=headers)
    elif method == "POST":
        return requests.post(endpoint, headers=headers, json=data)
    elif method == "PUT":
        return requests.put(endpoint, headers=headers, json=data)
    else:
        raise ValueError("Unsupported HTTP method")
