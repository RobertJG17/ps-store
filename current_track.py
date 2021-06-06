import pandas as pd
import plotly.graph_objects as go
from main import spotty


def curr_song_svg(song=None):
    song_info = pd.DataFrame.from_records(spotty.audio_features(song))
    attributes = song_info.drop(["type", "id", "tempo", "key", "mode",
                                 "uri", "track_href", "analysis_url",
                                 "duration_ms", "loudness", "time_signature"],
                                axis=1)

    track_name = spotty.track(song)['name']
    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(r=attributes.iloc[0],
                                  theta=attributes.columns,
                                  fill='toself',
                                  connectgaps=True,
                                  name=track_name))

    with open("current_song.svg", "w") as open_file:
        fig = fig.to_html()
        open_file.write(fig)
