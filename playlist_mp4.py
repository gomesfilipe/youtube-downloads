from downloads import downloadPlaylistAsMP4
import sys

try:
  if len(sys.argv) != 2:
    raise Exception('Wrong quantity of arguments.')

  playlistLink = sys.argv[1]  
  playlistLink = "link_here"
  downloadPlaylistAsMP4(playlistLink)

except Exception as error:
  print(error)
