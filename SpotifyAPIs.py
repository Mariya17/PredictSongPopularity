import spotipy

spotify = spotipy.Spotify()
artist_name = {}
track_name = {}
track_id = {}
popularity = {}

for i in range(0,10000,50):
    track_results = spotify.search(q='year:2018', type='track', limit=50,offset=i)
    for i, t in enumerate(track_results['tracks']['items']):
        artist_name.append(t['artists'][0]['name'])
        track_name.append(t['name'])
        track_id.append(t['id'])
        popularity.append(t['popularity'])