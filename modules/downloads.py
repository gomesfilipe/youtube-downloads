from pytube import YouTube
from pytube import Playlist
import os
import modules.log as log

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
    log.success()
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
    log.success()
  except:
    log.videoError(videoLink)
  finally:
    log.finish()

def downloadPlaylistAsMP4(playlistLink):
  try:
    playlist = Playlist(playlistLink)
    totalVideos = len(playlist)

    if totalVideos == 0:
      raise Exception()

  except:
    log.playlistError(playlistLink)
    log.finish()
    return

  folder = 'mp4-downloads'
  errors = []
  path = '{}/{}'.format(os.getcwd(), folder)

  try:
    os.mkdir(folder)
  except:
    pass

  for index, url in enumerate(playlist):
    try:
      log.progressAndErrors(index + 1, totalVideos, errors)
      YouTube(url).streams.filter(file_extension='mp4', progressive=True).first().download(path)
    except:
      errors.append(url)

  log.success()
  log.finish()

def downloadPlaylistAsMP3(playlistLink):
  try:
    playlist = Playlist(playlistLink)
    totalVideos = len(playlist)

    if totalVideos == 0:
      raise Exception()

  except:
    log.playlistError(playlistLink)
    log.finish()
    return

  folder = 'mp3-downloads'
  errors = []
  path = '{}/{}'.format(os.getcwd(), folder)

  try:
    os.mkdir(folder)
  except:
    pass

  for index, url in enumerate(playlist):
    try:
      log.progressAndErrors(index + 1, totalVideos, errors)
      outFile = YouTube(url).streams.filter(only_audio=True).first().download(path)
      _changeMP4ToMP3(outFile)
    except Exception as e:
      errors.append(url)

  log.success()
  log.finish()
