import requests
import pandas as pd
from sqlalchemy import create_engine

# ========== CONFIG ==========
API_KEY = "BUHceanXlftIAlWqWBGlORDH1A2bb7yX"  # Replace with your real key
engine = create_engine("mysql+pymysql://root:hollywood30@localhost/spotify_db")

# ========== FETCH EDM EVENTS ==========
url = "https://app.ticketmaster.com/discovery/v2/events.json"
params = {
    "apikey": API_KEY,
    "classificationName": "EDM",
    "countryCode": "US",
    "stateCode": "MA",
    "size": 100
}

response = requests.get(url, params=params)
data = response.json()

events = data.get("_embedded", {}).get("events", [])
event_list = []

for event in events:
    try:
        name = event.get("name", "N/A")
        date = event.get("dates", {}).get("start", {}).get("localDate", "")
        time = event.get("dates", {}).get("start", {}).get("localTime", "")
        datetime = f"{date} {time}".strip()
        
        artist = event.get("_embedded", {}).get("attractions", [{}])[0].get("name", "N/A")
        venue = event.get("_embedded", {}).get("venues", [{}])[0].get("name", "N/A")
        city = event.get("_embedded", {}).get("venues", [{}])[0].get("city", {}).get("name", "N/A")
        state = event.get("_embedded", {}).get("venues", [{}])[0].get("state", {}).get("name", "N/A")
        
        price_info = event.get("priceRanges", [{}])[0]
        min_price = price_info.get("min")
        max_price = price_info.get("max")
        median_price = (min_price + max_price) / 2 if min_price and max_price else None

        subgenre = event.get("classifications", [{}])[0].get("subGenre", {}).get("name", "N/A")

        event_list.append({
            "Artist": artist,
            "Event Name": name,
            "Venue": venue,
            "City": city,
            "State": state,
            "DateTime": datetime,
            "Median Ticket Price": median_price,
            "Subgenre": subgenre
        })
    except Exception as e:
        print(f"Skipping event due to error: {e}")

# ========== SAVE TO MYSQL ==========
tm_df = pd.DataFrame(event_list)
tm_df.columns = [col.replace(" ", "_") for col in tm_df.columns]  # Safe SQL column names

if not tm_df.empty:
    tm_df.to_sql("ticketmaster_events", con=engine, if_exists="replace", index=False)
    print("✅ Ticketmaster data saved to MySQL table 'ticketmaster_events'")
else:
    print("⚠️ No EDM events found in the API response.")
