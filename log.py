import os

def _percent(x, total):
  return 100 * (x / total)

def progress(x, total):
  os.system('clear')
  print('Progress: {}/{} ({}%)'.format(x, total, int(_percent(x, total))))

def finish():
  print('End of execution.')

def videoError(url):
  print('Download error: {}'.format(url))

def playlistError(url):
  print('Error acessing playlist: {}'.format(url))

def progressAndErrors(x, total, errorsUrls):
  os.system('clear')
  progress(x, total)

  for url in errorsUrls:
    videoError(url)