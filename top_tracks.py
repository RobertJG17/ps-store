from config import sp


ranges = ['short_term', 'medium_term', 'long_term']

results = sp.current_user_top_tracks(time_range=ranges[2], limit=50)

print(results)

top_track_ids = []

for result in results["items"]:
    track_id = result["uri"].split(":")[2]
    print(track_id)
    top_track_ids.append(track_id)
    # print("name: ", result["name"], "uri: ", result["uri"], "\n")

track_analysis = sp.audio_features(top_track_ids)

# for track in track_analysis:
#     print(track, '\n')