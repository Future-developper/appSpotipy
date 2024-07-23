import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

# date = input("What year would you like to travel in YYYY-MM-DD format?")
URL = "https://www.billboard.com/charts/hot-100/" + "date"
client_id = "98cb09b7c88943b4b7fb5da2eb450661"
client_secret = "89d92e117ee44feea4137ab30e379776"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri="https://localhost:8888/callback",
                                               scope="user-library-read"))# response = requests.get(URL)
taylor_uri = 'spotify:artist:06HL4z0CvFAxyc27GXpf02'

results = sp.artist_albums(taylor_uri, album_type='album')
albums = results['items']
while results['next']:
    results = sp.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])
# data = response.text
#
# soup = BeautifulSoup(data)
# "C:\Program Files\JetBrains\PyCharm Community Edition 2024.1.3\bin\pycharm64.exe"
#
# birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
# spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
#
# results = spotify.artist_albums(birdy_uri, album_type='album')
# albums = results['items']
# while results['next']:
#     results = spotify.next(results)
#     albums.extend(results['items'])
#
# for album in albums:
#     print(album['name'])