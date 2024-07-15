import requests
import os
from dotenv import load_dotenv, set_key

TOKEN_URL = 'https://api.genius.com/oauth/token'

def get_access_token(client_id, client_secret):
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }
    response = requests.post(TOKEN_URL, data=data)
    return response.json()

# Get the access token
if __name__ == "__main__":
    load_dotenv("../config/.env")
    CLIENT_ID = os.getenv('GENIUS_CLIENT_ID')
    CLIENT_SECRET = os.getenv('GENISU_CLIENT_SECRET')
    tokens = get_access_token(CLIENT_ID, CLIENT_SECRET)
    access_token = tokens.get('access_token')
    set_key("../config/.env", "GENIUS_API_TOKEN", access_token)
    print('Access Token:', access_token)