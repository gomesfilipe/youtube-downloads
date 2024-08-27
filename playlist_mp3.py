from modules.downloads import downloadPlaylistAsMP3
import sys
import modules.log as log

try:
  if len(sys.argv) != 2:
    raise Exception()

  playlistLink = sys.argv[1]
  downloadPlaylistAsMP3(playlistLink)

except:
  log.argumentError()
