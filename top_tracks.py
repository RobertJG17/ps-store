import spotipy
import numpy as np
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth="BQAaLF-uU4PtLTBRT-3a917vwE967OMkPOVMROCFdcbkgn-gkTqmNTF9EOjLnsuhCLL86-T--SFPJcMLI_ZoiYC2tfzF5iSjFiR2QmpvhDGhqQP-85G0JRkP6x3zzI5e_oP1nBFtajtMh2pwFySeKh3z0n1CEOShpecz6N5tbvk9WdEeXIWE5FYgGTZnj_xFIrq2Yo61pi3GamZ2cWIMBURhT_UHlxbPOw3rt_qn12KqI9WstUOyuCfRgFvPRmPq7twu5hvhRowD3r2xsWdW1cMqNLTj_oMo3sJtMX4t7Cbp")


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