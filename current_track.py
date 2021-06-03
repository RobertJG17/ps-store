from config import spotty
import pandas as pd
import plotly.graph_objects as go

song = spotty.currently_playing()['item']['id']
song_info = pd.DataFrame.from_records(spotty.audio_features(song))
attributes = song_info.drop(["type", "id", "tempo", "key", "mode",
                             "uri", "track_href", "analysis_url",
                             "duration_ms", "loudness", "time_signature"],
                            axis=1)

track_name = spotty.track(song)['name']
print(track_name)
fig = go.Figure()

fig.add_trace(go.Scatterpolar(r=attributes.iloc[0],
                              theta=attributes.columns,
                              fill='toself',
                              connectgaps=True,
                              name=track_name))
fig = fig.to_html()

with open("current_song.svg", "w") as open_file:
    open_file.write(fig)
    curr_song_svg = open_file
