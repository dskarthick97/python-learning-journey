"""
Scrapping the billboard and creating a spotify playlist.
"""

import lxml
import spotipy
import requests

from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth


# extract the html page data
date_ = input(
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD: "
)

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date_}/").text

# prepare the soup and extract the song titles
soup = BeautifulSoup(response, "lxml")
song_titles_tags = soup.find_all("h3", class_="a-no-trucate")
song_titles = [song_title_tag.get_text().strip() for song_title_tag in song_titles_tags]

# interact with the spotify api's using the spotipy module
SPOTIFY_CLIENT_ID = "fa2c1526f3264277b28b85e782e0e793"
SPOTIFY_CLIENT_SECRET = "d1c06c04e97545408d662e290c1308f7"
SPOTIFY_SCOPE = "playlist-modify-private"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri="https://example.com",
        scope=SPOTIFY_SCOPE,
        cache_path="token.txt",
    )
)

user_id = sp.current_user()["id"]

# preparing the song uri using the song titles.
song_uris = []
year = date_.split("-")[0]
for song_title in song_titles:
    result = sp.search(q=f"track:{song_title} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song_title} not found. Skipping it.")

# create a new playlist in the spotify and add all the song uri's in it.
playlist_id = sp.user_playlist_create(
    user=user_id,
    name=f"{date_} Billboard 100",
    public=False,
    description=f"Billboard's top 100 songs on {date_}",
)["id"]

res = sp.playlist_add_items(playlist_id, items=song_uris)
print(res)
