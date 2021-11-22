"""
Saving the cover image of the playlist.
"""

import spotipy

from spotipy.oauth2 import SpotifyOAuth

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

# user_id = sp.current_user()["id"]
playlist_id = "01M36iwmz7yzJPL9MYQeEy"


response = sp.playlist_cover_image(playlist_id)
print(response)
