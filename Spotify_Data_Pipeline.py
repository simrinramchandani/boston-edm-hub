# Spotify User Data Pipeline
# Goal: Create a table where each row is a user, with data from Spotify's Web API

import requests
import base64
import pandas as pd
from flask import Flask, request, redirect
import urllib.parse
from sqlalchemy import create_engine

# MySQL connection setup
engine = create_engine("mysql+pymysql://root:hollywood30@localhost/spotify_db")


app = Flask(__name__)

def stringify_lists(data):
    return {
        k: ', '.join(v) if isinstance(v, list) else v
        for k, v in data.items()
    }

# =====================
# Step 1: Config Setup
# =====================
CLIENT_ID = '6dc14caf1232420db0ea7f38ab654796'
CLIENT_SECRET = 'c1a77ea2cb784a138fefed07b551f042'
REDIRECT_URI = 'https://682d-2600-4040-526c-f100-9885-e718-e81a-ce57.ngrok-free.app/callback'
SCOPE = 'user-top-read user-library-read playlist-read-private user-follow-read user-read-email'

auth_url = "https://accounts.spotify.com/authorize"
token_url = "https://accounts.spotify.com/api/token"

# ======================
# Step 2: OAuth Flow
# ======================

@app.route('/')
def login():
    params = {
        "client_id": CLIENT_ID,
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "scope": SCOPE
    }
    return redirect(auth_url + "?" + urllib.parse.urlencode(params))

@app.route('/callback')
def callback():
    code = request.args.get('code')
    auth_str = f"{CLIENT_ID}:{CLIENT_SECRET}"
    b64_auth = base64.b64encode(auth_str.encode()).decode()

    headers = {
        "Authorization": f"Basic {b64_auth}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI
    }
    response = requests.post(token_url, headers=headers, data=data)
    token = response.json().get("access_token")
    
    # Step 3: Pull user data and build the profile row
    user_data = get_user_profile_data(token)
    user_data = stringify_lists(user_data)
    df = pd.DataFrame([user_data])
    df.to_sql("spotify_users", con=engine, if_exists="append", index=False)
    return "✅ User profile data saved as CSV. You can close this window."

# ============================
# Step 3: Collect User Data
# ============================

def get_user_profile_data(access_token):
    headers = {"Authorization": f"Bearer {access_token}"}

    def get(endpoint, params=None):
        r = requests.get(f"https://api.spotify.com/v1{endpoint}", headers=headers, params=params)
    
        if r.status_code != 200:
            print(f"❌ Spotify API error on {endpoint}: {r.status_code}")
            print(f"Response text: {r.text}")
            return {}

        try:
            return r.json()
        except ValueError:
            print(f"❌ Failed to parse JSON from {endpoint}")
            print("Response content:", r.content)
            return {}
    
    profile = get("/me")
    top_artists = get("/me/top/artists", {"limit": 5, "time_range": "long_term"}).get('items', [])
    top_tracks = get("/me/top/tracks", {"limit": 5, "time_range": "long_term"}).get('items', [])
    saved_tracks = get("/me/tracks", {"limit": 5}).get('items', [])
    followed_artists = get("/me/following?type=artist&limit=5").get('artists', {}).get('items', [])
    playlists = get("/me/playlists", {"limit": 5}).get('items', [])

    top_genres = list({genre for artist in top_artists for genre in artist.get('genres', [])})
    track_ids = [track['id'] for track in top_tracks if 'id' in track]
    audio_features = get("/audio-features", {"ids": ','.join(track_ids)}).get('audio_features', [])

    return {
        "User ID": profile.get('id'),
        "Display Name": profile.get('display_name'),
        "Email": profile.get('email'),
        "Country": profile.get('country'),
        "Top Artists": [a['name'] for a in top_artists],
        "Top Genres": top_genres,
        "Top Tracks": [t['name'] for t in top_tracks],
        "Saved Tracks": [s['track']['name'] for s in saved_tracks],
        "Followed Artists": [f['name'] for f in followed_artists],
        "Playlists": [p['name'] for p in playlists],
        "Audio Features (Danceability)": [af.get('danceability') for af in audio_features if af]
    }

if __name__ == '__main__':
    app.run(port=8888, debug=True)
