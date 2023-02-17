from modules.downloads import downloadVideoAsMP4
import sys
import modules.log as log

try:
  if len(sys.argv) != 2:
    raise Exception('Wrong quantity of arguments.')

  videoLink = sys.argv[1]  
  downloadVideoAsMP4(videoLink)

except:
  log.argumentError()
