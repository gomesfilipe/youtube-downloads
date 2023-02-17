from modules.downloads import downloadPlaylistAsMP4
import sys
import modules.log as log

try:
  print(sys.argv)
  if len(sys.argv) != 2:
    raise Exception()

  playlistLink = sys.argv[1]  
  downloadPlaylistAsMP4(playlistLink)

except:
  log.argumentError()
