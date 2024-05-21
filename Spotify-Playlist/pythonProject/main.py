import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="30182631f8cf4147b801a87254094825",
        client_secret="45b49f38a5fa431e99a02fe0d60da49f",
        show_dialog=True,
        cache_path="Token.txt",
        username="Zahed"
    )
)
user_id = sp.current_user()["id"]