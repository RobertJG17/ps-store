import spotipy
import numpy as np
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth="BQBRlvOHK-Jpl67q7K7bpNkUXFyXDmZVYYlvzxiUdQZ-hAqzoZz124l08pudjUNOf19i_g-ODSP5x14SaK8G1kESr0Wyvmb0zT9ehk_SvoaeBPmvLZwoNZSo1KX42Ftq1Vh6c7-gplgTGNTP5jMUlYR_SGGJB1RtO71x5NFG9hd1VSHkO91uG80AgdN1eZsUgH5vkSdCC3YM6gGK229AX0DkutFs5lIIx_KJh0NbkBwZTveD2Lr7i6dKftnRocj4NkeNoNuVpU_6hQf9reBuh8of9yOYjWbnXeqQzBVlCNEF")


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