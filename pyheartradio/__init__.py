import requests


class IHearthRadio:
    new_user_url = 'https://us.api.iheart.com/api/v1/account/loginOrCreateOauthUser'

    search_url = 'https://us.api.iheart.com/api/v3/search/all'

    # podcasts
    podcast_episodes_url = 'https://us.api.iheart.com/api/v3/podcast/podcasts/{podcast_id}/episodes'
    podcast_stream_url = 'https://us.api.iheart.com/api/v3/podcast/episodes/{episode_id}'

    # stations
    station_stream_url = 'https://us.api.iheart.com/api/v2/content/liveStations/{stream_id}'
    meta_url = 'https://us.api.iheart.com/api/v3/live-meta/stream/{stream_id}/currentTrackMeta'

    artist_url = 'https://us.api.iheart.com/api/v1/catalog/getArtistByArtistId?artistId={artist_id}'  # GET
    artist_profile_url = 'https://us.api.iheart.com/api/v3/artists/profiles/{artist_id}'  # GET
    similar_artists_url = 'https://us.api.iheart.com/api/v1/catalog/artist/{artist_id}/getSimilar'  # GET
    artist_albums_url = 'https://us.api.iheart.com/api/v3/catalog/artist/{artist_id}/albums'  # GET

    artist_playlist_url = 'https://us.api.iheart.com/api/v2/playlists/{user_id}/ARTIST/{artist_id}'  # POST formData = {'contentId':artist_id, 'playedFrom':10}
    artist_stream_url = 'https://us.api.iheart.com/api/v2/playback/streams'  # Takes steramId in POST params

    # NOTE useful track info - No stream available
    track_url = 'https://us.api.iheart.com/api/v1/catalog/getTrackByTrackId?trackId={track_id}'  # GET
    track2_url = 'https://us.api.iheart.com/api/v3/catalog/tracks/{track_id}'  # GET

    def search_stations(self, search_term):
        payload = {"keywords": search_term,
                   "maxRows": 10,
                   "bundle": "false",
                   "station": "true",
                   "artist": "false",
                   "track": "false",
                   "playlist": "false",
                   "podcast": "false"}
        # get the response from the IHeartRadio API
        search_res = requests.get(self.search_url, params=payload).json()
        for station in search_res["results"]["stations"]:

            station_name = station["name"]
            station_id = station["id"]

            # query the station URL using the ID
            url = self.station_stream_url.format(stream_id=station_id)
            station_res = requests.get(url).json()

            # Use the first stream URL
            for x in station_res["hits"][0]["streams"]:
                stream_url = station_res["hits"][0]["streams"][x]
                image = station_res["hits"][0]["logo"]
                description = station_res["hits"][0]["description"]
                yield {
                    "title": station_name,
                    "description": description,
                    "stream": stream_url,
                    "image": image,
                    "id": station_id
                }
                break

    def search_podcast(self, search_term):
        payload = {"keywords": search_term,
                   "maxRows": 10,
                   "bundle": "false",
                   "station": "false",
                   "artist": "false",
                   "track": "false",
                   "playlist": "false",
                   "podcast": "true"}
        # get the response from the IHeartRadio API
        search_res = requests.get(self.search_url, params=payload).json()
        for podcast in search_res["results"]["podcasts"]:
            name = podcast["title"]
            podcast_id = podcast["id"]
            image = podcast["image"]
            desc = podcast["description"]
            yield {
                "title": name,
                "image": image,
                "description": desc,
                "id": podcast_id
            }

    def get_podcast_episodes(self, podcast_id):
        url = self.podcast_episodes_url.format(podcast_id=podcast_id)
        res = requests.get(url).json()
        for episode in res["data"]:
            episode_id = episode["id"]
            episode_title = episode["title"]
            episode_duration = episode["duration"]
            episode_desc = episode["description"]
            episode_image = episode['imageUrl']
            ts = episode['startDate']

            url = self.podcast_stream_url.format(episode_id=episode_id)
            res = requests.get(url).json()
            episode_stream = res["episode"]["mediaUrl"]
            yield {
                "title": episode_title,
                "duration": episode_duration,
                "image": episode_image,
                "id": episode_id,
                "description": episode_desc,
                "stream": episode_stream
            }

    # WIP (no streams)
    def search_track(self, search_term):
        payload = {"keywords": search_term,
                   "maxRows": 10,
                   "bundle": "false",
                   "station": "false",
                   "artist": "false",
                   "track": "true",
                   "playlist": "false",
                   "podcast": "false"}
        # get the response from the IHeartRadio API
        search_res = requests.get(self.search_url, params=payload).json()
        for track in search_res["results"]["tracks"]:
            name = track["title"]
            track_id = track["id"]
            artist = track["artistName"]
            album = track["albumName"]
            artist_id = track["artistId"]
            album_id = track["albumId"]
            image = track["image"]
            yield {
                "title": name,
                "album": album,
                "artist": artist,
                "image": image,
                "id": track_id,
                "artist_id": artist_id,
                "album_id": album_id
            }

    def search_artist(self, search_term):
        payload = {"keywords": search_term,
                   "maxRows": 10,
                   "bundle": "false",
                   "station": "false",
                   "artist": "true",
                   "track": "false",
                   "playlist": "false",
                   "podcast": "false"}
        # get the response from the IHeartRadio API
        search_res = requests.get(self.search_url, params=payload).json()
        for artist in search_res["results"]["artists"]:
            name = artist["name"]
            artist_id = artist["id"]
            image = artist["image"]

            url = self.artist_profile_url.format(artist_id=artist_id)
            res = requests.get(url).json()

            tracks = res["tracks"]
            albums = res["albums"]
            related_artists = res["relatedTo"]
            yield {
                "title": name,
                "albums": albums,
                "artist": artist,
                "image": image,
                "id": artist_id,
                "tracks": tracks,
                "related_artist": related_artists
            }

    def search_playlist(self, search_term):
        payload = {"keywords": search_term,
                   "maxRows": 10,
                   "bundle": "false",
                   "station": "false",
                   "artist": "false",
                   "track": "false",
                   "playlist": "true",
                   "podcast": "false"}
        # get the response from the IHeartRadio API
        search_res = requests.get(self.search_url, params=payload).json()
        for playlist in search_res["results"]["playlists"]:
            name = playlist["name"]
            playlist_id = playlist["id"]
            desc = playlist["description"]
            image = playlist["urls"].get("image")
            url = playlist["urls"].get("web")
            play = playlist["urls"].get("play")
            yield {
                "title": name,
                "url": url,
                "description": desc,
                "image": image,
                "id": playlist_id
            }


