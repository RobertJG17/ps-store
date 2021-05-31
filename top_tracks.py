import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth="BQARNVdE3z-4k6WvEUYPihU19NWMgcpZCHtY5HwUZ_Gazz8PWQB-fGs0YHsbM-bjqh9_GjkwJiULxn2k34MFRY5j_YNUJGG4Z8OrBth_T1F0IuSxyTq5PIy4dHD-2fbTQ4EMaoXl4oq1SAhs_Iz2mBCWtClkIYRt9PV-8t-4x434HNhUVVUV-50kuvVrSaqywIuPkdtkBcHh07COVgb4ajZBuI0GzsdIH4GHPmzjBjzn2eQGy8-MBvRp1TBPi-vpoIlxTR41l5IhDVmQlOEfEAuqT2CubxyrIvZ0Ikks82f1")


ranges = ['short_term', 'medium_term', 'long_term']

results = sp.current_user_top_tracks(time_range=ranges[1], limit=50)

top_track_ids = []

for result in results["items"]:
    track_id = result["uri"].split(":")[2]
    print(track_id)
    top_track_ids.append(track_id)
    # print("name: ", result["name"], "uri: ", result["uri"], "\n")

track_analysis = sp.audio_features(top_track_ids)

for track in track_analysis:
    print(track, '\n')