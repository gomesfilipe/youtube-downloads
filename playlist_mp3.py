from downloads import downloadPlaylistAsMP3
import sys

try:
  if len(sys.argv) != 2:
    raise Exception('Wrong quantity of arguments.')

  playlistLink = sys.argv[1]  
  playlistLink = "link_here"
  downloadPlaylistAsMP3(playlistLink)

except Exception as error:
  print(error)
