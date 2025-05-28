# Boston EDM Hub

This project pulls data from Spotify and Ticketmaster to create a SQL database focused on the EDM scene in Boston. It connects artists, events, playlists, and user preferences to help recommend events and explore music trends.

## 🛠 Tools  
- MySQL  
- SQL  
- Python  
- Spotify Web API  
- Ticketmaster API  
- pandas, SQLAlchemy, Flask, requests  


## 📁 Files  
### SQL Files  
- `spotify_db_edm_artists.sql`: EDM artists table and sample data  
- `spotify_db_spotify_users.sql`: Spotify user data  
- `spotify_db_ticketmaster_events.sql`: Event listings from Ticketmaster  
- `spotify_db_user_event_interest.sql`: Tracks events users interacted with  
- `spotify_db_user_playlists.sql`: User playlists and genres  
- `group06_queries.sql`: SQL queries for recommendations and analysis  

### Python Scripts  
- `artists_api.py`: Gets artist data from Spotify and Setlist.fm  
- `Spotify_Data_Pipeline.py`: Collects Spotify user data through OAuth  
- `ticketmaster.py`: Pulls EDM events from Ticketmaster  


## 📌 What We Did  
- Built a connected database for users, artists, events, and playlists  
- Wrote SQL queries to recommend events based on listening history  
- Looked at top venues and genres in the Boston EDM scene  
- Automated data collection using Python scripts and APIs  


## 🖼️ Sample Visualization  
Here’s the ER diagram showing how the tables in our database are connected:

![ER Diagram](er%20diagram.png)

