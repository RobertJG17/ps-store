from spotipy import SpotifyOAuth, Spotify
import os
from os.path import join, dirname
from dotenv import load_dotenv

# Pulling data from env file
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Unique access tokens from env files
cid = os.environ.get("USER_ID")
secret = os.environ.get("USER_CLIENT")

# OAUTH FLOW (LONG TERM USAGE i.e. having user sign in to gather user information)
scope = 'user-top-read'

auth_manager = SpotifyOAuth(client_id=cid,
                            client_secret=secret,
                            redirect_uri='http://127.0.0.1:5000/',
                            scope=scope)

spotty = Spotify(auth_manager=auth_manager)

# spotty = spotipy.Spotify(auth=token)
# token = 'BQCsPmPkP37yHZ4w63BFgT3I--TnKDiVD6ZegIq73r6zdl1EZau_xj1OaWdWd7INZ1mIrwGHLkH5w_sgVCs4UuBFZXr-j5A0pHjin3TcH4C57Gvd-e-13-4u7jRIPCJ5-rpGQnEGtpUzFB8EiDJo9KtWlmg2zV3pUsEQUjvQkqaO8ukULgp65HsqA_ZzZM3bgsAB5ECYboHVWSeNllU20JdSXCT7PHQ05arJjqSysuwhjhou9C6BtfY7Io5ktY06qnEo7J8YzYX_5fIwiKRwrNCv3-r6MNHzBWPjp8TtNUVs'
# print("this sp -->", sp.current_user_top_artists(time_range=ranges[2], limit=50))
