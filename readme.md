# PyHeartRadio

Python api for [iHeartRadio](https://www.iheart.com/)

## Install

```bash
pip install pyheartradio
```

## Usage

```python
from pyheartradio import IHearthRadio

radio = IHearthRadio()

for s in radio.search_stations("rock"):
    print(s)
    #{'title': '98 ROCK Tampa', 'description': "Tampa Bay's Rock Station",
    # 'stream': 'http://stream.revma.ihrhls.com/zc697/hls.m3u8',
    # 'image': 'https://i.iheart.com/v3/re/new_assets/5d6542f731cd95618c92d7dc',
    # 'id': 697}

for s in radio.search_podcast("heavy metal hangover"):
    print(s)
    # {'title': 'The Heavy Metal Hangover',
    # 'image': 'https://i.iheart.com/v3/url/aHR0cHM6Ly9wYmNkbjEucG9kYmVhbi5jb20vaW1nbG9nby9pbWFnZS1sb2dvLzI0NDk2NTUvdGh1bWJuYWlsLmpwZw==',
    # 'description': 'Heavy metal podcast where the beer is always cold and the music is always heavy.',
    # 'id': 70625669}
    for episode in radio.get_podcast_episodes(s["id"]):
        print(episode)
        #{'title': 'Episode 191 -   T. Ferguson',
        # 'duration': 8482,
        # 'image': 'https://i.iheart.com/v3/url/aHR0cHM6Ly9wYmNkbjEucG9kYmVhbi5jb20vaW1nbG9nby9pbWFnZS1sb2dvLzI0NDk2NTUvdGh1bWJuYWlsLmpwZw',
        # 'id': 87107553,
        # 'description': '<p>This week Chris and J talk about bands with funny names.\xa0\xa0</p>\n\n<p>Our picks of the week:\xa0J - Carcass - Torn Arteries;\xa0Chris - Rage - Resurrection Day\n</p>\n\n<p>\xa0</p>\n\n<p>How to Subscribe to the show:\xa0<a href="https://itunes.apple.com/us/podcast/the-heavy-metal-hangover/id1341478459?mt&#61;2&amp;ls&#61;1">Itunes</a>\xa0<a href="https://www.google.com/podcasts?feed&#61;aHR0cHM6Ly90aGVoZWF2eW1ldGFsaGFuZ292ZXIucG9kYmVhbi5jb20vZmVlZC8%3D">Google Podcasts</a>\xa0<a href="https://www.stitcher.com/s?fid&#61;168787&amp;refid&#61;stpr">Stitcher</a>\xa0<a href="https://open.spotify.com/show/3jE9Jcz7eL9vdBuw2w1RSR">Spotify</a>\xa0</p>\n\n<p>Follow The Heavy Metal Hangover on Social Media:\xa0\xa0<a href="https://www.instagram.com/theheavymetalhangover/">Instagram</a>\xa0<a href="https://www.facebook.com/theheavymetalhangover/">Facebook</a></p>',
        # 'stream': 'https://mcdn.podbean.com/mf/web/xfkq4f/HMH191-TurdFerguson.mp3?source=iheart'}

```