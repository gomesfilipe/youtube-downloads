from pytube import YouTube
from pytube import Playlist
import os
import log

def _changeMP4ToMP3(file):
  base, ext = os.path.splitext(file)
  newFile = base + '.mp3'
  os.rename(file, newFile)

def downloadVideoAsMP4(videoLink):
  folder = 'mp4-downloads'
  try:
    os.mkdir(folder)
  except:
    pass
  
  try:
    path = '{}/{}'.format(os.getcwd(), folder)
    YouTube(videoLink).streams.filter(file_extension='mp4', progressive=True).first().download(path)
  except:
    log.videoError(videoLink)
  finally:
    log.finish()

def downloadVideoAsMP3(videoLink):
  folder = 'mp3-downloads'
  try:
    os.mkdir(folder)
  except:
    pass
  
  try:
    path = '{}/{}'.format(os.getcwd(), folder)
    outFile = YouTube(videoLink).streams.filter(only_audio=True).first().download(path)
    _changeMP4ToMP3(outFile)
  except:
    log.videoError(videoLink)
  finally:
    log.finish()

def downloadPlaylistAsMP4(playlistLink):
  folder = 'mp4-downloads'
  try:
    os.mkdir(folder)
  except:
    pass
  
  try:
    playlist = Playlist(playlistLink)
    totalVideos = len(playlist)
  except:
    log.playlistError(playlistLink)
    log.finish()
    return
    
  errors = []
  path = '{}/{}'.format(os.getcwd(), folder)

  for index, url in enumerate(playlist):
    try:
      log.progressAndErrors(index + 1, totalVideos, errors)
      YouTube(url).streams.filter(file_extension='mp4', progressive=True).first().download(path)
    except:
      errors.append(url)

  log.finish()

def downloadPlaylistAsMP3(playlistLink):
  folder = 'mp4-downloads'
  try:
    os.mkdir(folder)
  except:
    pass
  
  try:
    playlist = Playlist(playlistLink)
    totalVideos = len(playlist)
  except:
    log.playlistError(playlistLink)
    log.finish()
    return
  
  errors = []
  path = '{}/{}'.format(os.getcwd(), folder)

  for index, url in enumerate(playlist):
    try:
      log.printProgress(index + 1, totalVideos)
      outFile = YouTube(url).streams.filter(only_audio=True).first().download(path)
      _changeMP4ToMP3(outFile)
    except:
      errors.append(url)
  
  log.finish()

# TODO
# Ver como baixar com a maior qualidade disponível;
# Testar tudo (fazer playlist de teste);
# Fazer README explicando como instalar as dependências e utilizar os scripts;
