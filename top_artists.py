from config import sp
import pandas as pd


ranges = ['short_term', 'medium_term', 'long_term']

results = sp.current_user_top_artists(time_range=ranges[2], limit=50)
artists = pd.DataFrame.from_records(results["items"])


