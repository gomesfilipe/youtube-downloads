from downloaders.core.downloader import Downloader
from pytube import YouTube, Playlist
from helpers.utils import full_path
from enums.file_extension import FileExtension
import os

class PyTubeDownloader(Downloader):
  def download_video(self, video_link: str, path: str) -> bool:
    return self.__download_video(video_link, path, FileExtension.MP4, False)

  def download_audio(self, video_link: str, path: str) -> bool:
    return self.__download_video(video_link, path, FileExtension.MP3, True)

  def download_video_playlist(self, playlist_link: str, path: str) -> bool:
    playlist = Playlist(playlist_link)

    for video_link in playlist:
      self.download_video(self, video_link, path)

    return True

  def download_audio_playlist(self, playlist_link: str, path: str) -> bool:
    playlist = Playlist(playlist_link)

    for video_link in playlist:
      self.download_audio(self, video_link, path)

    return True

  def __download_video(self, video_link: str, path: str, file_extension: FileExtension, only_audio: bool) -> bool:
    try:
      YouTube(video_link).streams\
        .filter(file_extension = file_extension.value, only_audio = only_audio)\
        .first()\
        .download(full_path(path))
    except Exception:
      return False

    return True
