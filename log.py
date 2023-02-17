import os

def _percent(x, total):
  return 100 * (x / total)

def printProgress(x, total):
  os.system('clear')
  print('Progress: {}/{} ({}%)'.format(x, total, int(_percent(x, total))))

def printFinish():
  print('End of execution')
