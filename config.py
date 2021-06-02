import spotipy
import os

from os.path import join, dirname



# Unique access tokens from env files
# cid = os.environ.get("USER_ID")
# secret = os.environ.get("USER_CLIENT")

# OAUTH FLOW (LONG TERM USAGE i.e. having user sign in to gather user information)
scope = 'user-top-read'
# auth_manager = SpotifyOAuth(client_id=cid, client_secret=secret, scope=scope)

# client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)

sp = spotipy.Spotify(auth="BQAYzDXJ-hzaz2Drs39jg6n5cRQ2F5QJGHVnZQI7dvCQkWRUYjYAWpQWxdsae7TOGMlOCzv6gFAmWj4MqPReTt9CWRThLHavyJPCOggeNtoMFHz8HtqRcoDKI01KgvgcOV25ld6vSCPwBVWFu0PaZzo2x-LkhhUbUTvNe8Q6uWnBOe9wJtexVJqAN1Pb5_CgAhXOS8vXWBFNwRrFx_svZ__5Net9c-xesvSKvOV4qMj04ncL1-xQxjbk7yoL8ImhzdcuWN02eE3LOSPiHwFYkKk-k4uWkuQCxSdfGDVS5Wgv")

ranges = ['short_term', 'medium_term', 'long_term']
#
# print("this sp -->", sp.current_user_top_artists(time_range=ranges[2], limit=50))

