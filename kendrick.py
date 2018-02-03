import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from collections import OrderedDict
from datetime import datetime

client_id = 'c5c313824e2d4d55af503c4fcde096ab'
client_secret = 'b9d0930596134732a657981a7bcaab69'
redirect_uri = 'http://localhost:8888/callback'

client_credentials_manager = SpotifyClientCredentials(client_id,client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

scope = 'user-follow-read user-library-read'
# scope = 'user-library-read'



# if len(sys.argv) > 1:
#     username = sys.argv[1]
# else:
#     print "Usage: %s username" % (sys.argv[0],)
#     sys.exit()

# token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

print '''
<!DOCTYPE html>
<html>
<body>
<ul>
'''
start = datetime.now()
sp = spotipy.Spotify()


count = 0
releases = {}
urls = {}
lastid = 'spotify:artist:2YZyLoL8N0Wb9xBt1NhZWg'

albums = sp.artist_albums(lastid)#,album_type='album')
albums = albums['items']
uniqueAlbums = set()
for album in albums:
  album = album['id']
  uniqueAlbums.add(album)

for album in uniqueAlbums:
  album = sp.album(album)
  releases[album['name']+" - Kendrick - "+album['album_type']] = album['release_date']
  urls[album['name']+" - Kendrick - "+album['album_type']] = album['external_urls']['spotify']


ordered = OrderedDict(sorted(releases.items(), key=lambda t: t[1], reverse=True))

for item in ordered:
  print '<li><a href="',urls[item].encode("utf-8"),'"">',ordered[item].encode("utf-8"), item.encode("utf-8"),'</a></li>'

print '</ul>'
print '<h2>'
print count
print 'total time',datetime.now()-start
print '</h2>'

print '''
</html>
</body>
'''
