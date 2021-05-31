import config

scope = 'user-top-read'
ranges = ['short_term', 'medium_term', 'long_term']

sp = config.sp
results = sp.current_user_top_artists(time_range=ranges[2], limit=50)


print(results)
# for result in results:
#     print(result)