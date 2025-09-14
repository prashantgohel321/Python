# Day 46: Musical Time Machine

Welcome to my log for Day 46! This was a really fun and nostalgic project. I built a **Musical Time Machine** that can take me back to any date and create a Spotify playlist of the top 100 songs from that day. The project was an excellent real-world application that combined the web scraping skills I learned with `BeautifulSoup` and the API skills I developed, this time interacting with the **Spotify API** via the `Spotipy` library.


## Table of Contents
- [1. Project Goal: The Musical Time Machine](#1-project-goal-the-musical-time-machine)
- [2. Step 1: Scraping the Billboard Hot 100](#2-step-1-scraping-the-billboard-hot-100)
- [3. Step 2: Authenticating with the Spotify API](#3-step-2-authenticating-with-the-spotify-api)
- [4. Step 3: Searching for Songs on Spotify](#4-step-3-searching-for-songs-on-spotify)
- [5. Step 4: Creating the Spotify Playlist](#5-step-4-creating-the-spotify-playlist)
- [6. Day 46 Project: Musical Time Machine Code](#6-day-46-project-musical-time-machine-code)

---

### 1. Project Goal: The Musical Time Machine
The objective was to create a Python script that asks the user for a date, finds the Billboard Hot 100 chart for that date, and then automatically generates a new Spotify playlist containing those 100 songs. This is a perfect gift or a great way to rediscover music from a specific time.

---

### 2. Step 1: Scraping the Billboard Hot 100
The first task was to get the list of top 100 songs from a specific date.
-   **URL Structure:** I analyzed the Billboard Hot 100 chart URL and found that I could simply append a date in `YYYY-MM-DD` format to get the chart for that day.
-   **Scraping with BeautifulSoup:** I used the `requests` library to fetch the HTML content of the Billboard chart page. Then, I used `BeautifulSoup` to parse the HTML. By inspecting the page's source code, I identified that all song titles were located within `<h3>` tags inside a specific `<li><ul><li>` structure.
-   **List Comprehension:** I used a list comprehension to efficiently loop through all the selected elements and extract the text (the song titles), creating a Python list of 100 songs.

---

### 3. Step 2: Authenticating with the Spotify API
To interact with a user's Spotify account (even my own), I needed to go through their authentication process.
-   **Spotipy Library:** Instead of handling the complex OAuth 2.0 flow manually, I used `Spotipy`, a popular Python library that simplifies interaction with the Spotify API.
-   **Spotify Developer Account:** I created a developer account on Spotify's developer dashboard, registered a new application, and obtained a unique `Client ID` and `Client Secret`.
-   **Authorization:** I used `Spotipy`'s `SpotifyOAuth` to handle the authentication. This process involved specifying the required "scope" (`playlist-modify-private`), which grants my script permission to create private playlists. The first time the script runs, it opens a browser window for me to grant permission, then redirects to a specified URL. I copied this URL back into the console to complete the authentication, and `Spotipy` automatically cached the token for future use.

---

### 4. Step 3: Searching for Songs on Spotify
Once authenticated, I needed to find each of the 100 scraped songs on Spotify.
-   **Search Query:** I looped through my list of song titles from Billboard. For each song, I used `Spotipy`'s `sp.search()` method. To get more accurate results, I constructed a query that included the track name and the year from the user's input (e.g., `track:Bohemian Rhapsody year:1975`).
-   **Getting Song URIs:** The search result is a JSON object. I parsed it to get the URI (Uniform Resource Identifier) for each track, which is Spotify's unique identifier for a song.
-   **Error Handling:** Some songs from the past might not be available on Spotify. I wrapped my search logic in a `try-except` block to handle `IndexError`, which would occur if a search returned no results. This prevented the program from crashing and allowed it to simply skip any songs it couldn't find.

---

### 5. Step 4: Creating the Spotify Playlist
The final step was to create a new playlist and add all the song URIs I had collected.
-   **Create a Playlist:** I used the `sp.user_playlist_create()` method, passing in my user ID, a name for the playlist (e.g., "2000-08-12 Billboard 100"), and setting `public=False` to make it private.
-   **Add Tracks:** This method returns a dictionary containing the new playlist's ID. I then used the `sp.playlist_add_items()` method, passing in the playlist ID and my list of song URIs to add all the songs in one go.

The result is a brand new, nostalgic playlist waiting in my Spotify account!

---

### 6. Day 46 Project: Musical Time Machine Code
Here is the final code for the project:

```python
# main.py
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

# --- Environment Variables for Spotify API ---
SPOTIPY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = "[http://example.com](http://example.com)"
SPOTIFY_USERNAME = os.environ.get("SPOTIFY_USERNAME")

# --- Scraping Billboard Hot 100 ---
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
billboard_url = f"[https://www.billboard.com/charts/hot-100/](https://www.billboard.com/charts/hot-100/){date}"

response = requests.get(billboard_url)
soup = BeautifulSoup(response.text, 'html.parser')
song_titles_h3 = soup.select("li ul li h3")
song_titles = [song.getText().strip() for song in song_titles_h3]

# --- Spotify Authentication ---
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=SPOTIPY_REDIRECT_URI,
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=SPOTIFY_USERNAME,
    )
)
user_id = sp.current_user()["id"]

# --- Searching Spotify for Songs ---
song_uris = []
year = date.split("-")[0]
for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"'{song}' doesn't exist in Spotify. Skipped.")

# --- Creating and Adding to Spotify Playlist ---
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

print(f"New playlist '{date} Billboard 100' created successfully!")
```
