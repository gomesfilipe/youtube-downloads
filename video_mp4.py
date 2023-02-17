from downloads import downloadVideoAsMP4
import sys

try:
  if len(sys.argv) != 2:
    raise Exception('Wrong quantity of arguments.')

  videoLink = sys.argv[1]  
  videoLink = "https://www.youtube.com/watch?v=bRuXydQSw2Q&ab_channel=PeterBence"
  downloadVideoAsMP4(videoLink)

except Exception as error:
  print(error)
