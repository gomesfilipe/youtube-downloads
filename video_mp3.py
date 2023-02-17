from modules.downloads import downloadVideoAsMP3
import sys
import modules.log as log

try:
  if len(sys.argv) != 2:
    raise Exception()

  videoLink = sys.argv[1]  
  downloadVideoAsMP3(videoLink)

except:
  log.argumentError()
