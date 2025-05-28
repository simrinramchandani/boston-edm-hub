import requests
import pandas as pd
import time
import base64
from sqlalchemy import create_engine

# ========== CONFIG ==========
CLIENT_ID = '6dc14caf1232420db0ea7f38ab654796'
CLIENT_SECRET = 'c1a77ea2cb784a138fefed07b551f042'

# Get Spotify Bearer Token using Client Credentials Flow
def get_spotify_token(client_id, client_secret):
    auth_response = requests.post(
        'https://accounts.spotify.com/api/token',
        headers={
            'Authorization': 'Basic ' + base64.b64encode(f'{client_id}:{client_secret}'.encode()).decode()
        },
        data={
            'grant_type': 'client_credentials'
        }
    )

    if auth_response.status_code == 200:
        return auth_response.json()['access_token']
    else:
        raise Exception("Failed to get Spotify token: " + auth_response.text)

SPOTIFY_TOKEN = get_spotify_token(CLIENT_ID, CLIENT_SECRET)
HEADERS_SPOTIFY = {
    "Authorization": f"Bearer {SPOTIFY_TOKEN}"
}

LASTFM_API_KEY = 'ba68f5d5c509450b6e398fe6142ca218'
SETLISTFM_API_KEY = 'zqamxP19a8L92G8a9mLQggK16iWmJqg8k_G3'

HEADERS_SETLISTFM = {
    "x-api-key": SETLISTFM_API_KEY,
    "Accept": "application/json"
}

# ========== EDM ARTIST LIST (EXPANDED TO 100) ==========
edm_artists = [
    "Calvin Harris", "David Guetta", "Martin Garrix", "Zedd", "Kygo", "The Chainsmokers", "Tiesto", "Skrillex", "Marshmello", "Alesso",
    "Illenium", "Diplo", "Steve Aoki", "Avicii", "Deadmau5", "Afrojack", "Hardwell", "Armin van Buuren", "Alan Walker", "KSHMR",
    "Don Diablo", "Madeon", "Bassnectar", "REZZ", "Seven Lions", "ODESZA", "Slushii", "RL Grime", "Subtronics", "NGHTMRE",
    "San Holo", "Porter Robinson", "Gryffin", "Yellow Claw", "DJ Snake", "Dillon Francis", "Tchami", "Malaa", "Virtual Riot", "Excision",
    "Borgeous", "Krewella", "Louis The Child", "Said The Sky", "What So Not", "Deorro", "Big Gigantic", "Boombox Cartel", "Kayzo", "Getter",
    "Flume", "Madeon", "Cash Cash", "Felix Jaehn", "Klingande", "Matoma", "Robin Schulz", "Lost Frequencies", "Sigala", "Cheat Codes",
    "Galantis", "Lucas & Steve", "R3HAB", "Vinai", "Blasterjaxx", "W&W", "Benny Benassi", "Laidback Luke", "Breathe Carolina", "NERVO",
    "Showtek", "Boys Noize", "Pegboard Nerds", "Moksi", "Fox Stevenson", "TroyBoi", "Tritonal", "Vicetone", "DVBBS", "Curbi",
    "Brooks", "Sander van Doorn", "Firebeatz", "Noisecontrollers", "Kura", "Quintino", "Tommy Trash", "3LAU", "CID", "Crankdat",
    "Ookay", "Jauz", "Kill The Noise", "Bear Grillz", "ATLiens", "Noisia", "Kill Paris", "A-Trak", "Shiba San", "Black Tiger Sex Machine", 
    "Austin Millz"
]

# ========== FUNCTIONS ==========
def get_spotify_artist(artist_name):
    search_url = "https://api.spotify.com/v1/search"
    params = {"q": artist_name, "type": "artist", "limit": 1}
    r = requests.get(search_url, headers=HEADERS_SPOTIFY, params=params)
    items = r.json().get("artists", {}).get("items", [])
    return items[0] if items else None

def get_top_track(artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks"
    params = {"market": "US"}
    r = requests.get(url, headers=HEADERS_SPOTIFY, params=params)
    tracks = r.json().get("tracks", [])
    return tracks[0]['name'] if tracks else None

def get_top_album(artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/albums"
    params = {"include_groups": "album", "market": "US", "limit": 5}
    r = requests.get(url, headers=HEADERS_SPOTIFY, params=params)
    albums = r.json().get("items", [])
    return albums[0]['name'] if albums else None

def get_newest_release(artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/albums"
    params = {"market": "US", "limit": 5, "include_groups": "single,album"}
    r = requests.get(url, headers=HEADERS_SPOTIFY, params=params)
    albums = sorted(r.json().get("items", []), key=lambda x: x['release_date'], reverse=True)
    return albums[0]['name'] if albums else None

def get_listeners_lastfm(artist_name):
    url = f"http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist={artist_name}&api_key={LASTFM_API_KEY}&format=json"
    r = requests.get(url)
    listeners = r.json().get("artist", {}).get("stats", {}).get("listeners")
    return int(listeners) if listeners else 0

def get_concerts_setlistfm(artist_name):
    url = f"https://api.setlist.fm/rest/1.0/search/setlists?artistName={artist_name}&p=1"
    r = requests.get(url, headers=HEADERS_SETLISTFM)
    setlists = r.json().get("setlist", [])
    return [s['venue']['name'] for s in setlists[:3]] if setlists else []

# ========== MAIN LOOP ==========
data = []

for artist in edm_artists:
    print(f"Fetching data for {artist}...")
    try:
        artist_obj = get_spotify_artist(artist)
        if not artist_obj:
            continue
        artist_id = artist_obj['id']
        country = 'N/A'  # Spotify does not provide country
        genres = ', '.join(artist_obj.get('genres', []))

        row = {
            "Artist": artist,
            "Monthly Listeners (Last.fm)": get_listeners_lastfm(artist),
            "Top Song": get_top_track(artist_id),
            "Top Album": get_top_album(artist_id),
            "Newest Release": get_newest_release(artist_id),
            "Country": country,
            "Subgenre": genres,
            "Concerts": ', '.join(get_concerts_setlistfm(artist))
        }
        data.append(row)
        time.sleep(0.5)  # Be kind to APIs
    except Exception as e:
        print(f"Error fetching data for {artist}: {e}")

# ========== EXPORT ==========
edm_df = pd.DataFrame(data)
edm_df.to_csv("top_edm_artists_combined.csv", index=False)
print("✅ EDM artist data saved to top_edm_artists_combined.csv")

# ========== SAVE TO MYSQL ==========
engine = create_engine("mysql+pymysql://root:hollywood30@localhost/spotify_db")
edm_df.to_sql("edm_artists", con=engine, if_exists="replace", index=False)
print("✅ EDM artist data saved to MySQL table 'edm_artists'")