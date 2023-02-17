from pytube import YouTube
from pytube import Playlist
import os
import log

def _changeMP4ToMP3(file):
  base, ext = os.path.splitext(file)
  newFile = base + '.mp3'
  os.rename(file, newFile)

def downloadVideoAsMP4(videoLink, path):
  YouTube(videoLink).streams.filter(file_extension='mp4', progressive=True).first().download(path)
  log.printFinish()

def downloadVideoAsMP3(videoLink, path):
  outFile = YouTube(videoLink).streams.filter(only_audio=True).first().download(path)
  _changeMP4ToMP3(outFile)
  log.printFinish()

def downloadPlaylistAsMP4(playlistLink, path):
  playlist = Playlist(playlistLink)

  totalVideos = len(playlist)

  for index, url in enumerate(playlist):
    log.printProgress(index + 1, totalVideos)

    YouTube(url).streams.filter(file_extension='mp4', progressive=True).first().download(path)
  
  log.printFinish()

def downloadPlaylistAsMP3(playlistLink, path):
  playlist = Playlist(playlistLink)
  totalVideos = len(playlist)

  for index, url in enumerate(playlist):
    log.printProgress(index + 1, totalVideos)
    outFile = YouTube(url).streams.filter(only_audio=True).first().download(path)
    _changeMP4ToMP3(outFile)
  
  log.printFinish()

# TODO
# Ver como baixar com a maior qualidade disponível;
# ARGC ARGV para os scripts;
# Colocar try except nas funções;
# Testar tudo;
# Fazer README explicando como instalar as dependências e utilizar os scripts;
