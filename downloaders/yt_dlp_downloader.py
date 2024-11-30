from downloaders.core.downloader import Downloader
from helpers.utils import full_path
import os
from typing import Dict
import yt_dlp
from enums.file_extension import FileExtension

class YtDlpDownloader(Downloader):
  def download_video(self, video_link: str, path: str) -> bool:
    return self.__download(video_link, path, FileExtension.MP4, False)

  def download_audio(self, video_link: str, path: str) -> bool:
    return self.__download(video_link, path, FileExtension.MP3, False)

  def download_video_playlist(self, playlist_link: str, path: str) -> bool:
    return self.__download(playlist_link, path, FileExtension.MP4, True)

  def download_audio_playlist(self, playlist_link: str, path: str) -> bool:
    return self.__download(playlist_link, path, FileExtension.MP3, True)

  def __download(self, link: str, path: str, file_extension: FileExtension, is_playlist: bool) -> bool:
    options: Dict[str, str] = self.__options(file_extension, path, is_playlist)

    try:
      with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([link])
    except Exception:
      return False

    return True

  def __options(self, file_extension: FileExtension, path: str, is_playlist: bool) -> Dict[str, object]:
    types = {
      FileExtension.MP4: {
        'format': 'best',
        'outtmpl': os.path.join(path , '%(title)s.%(ext)s'),
        'noplaylist': not is_playlist,
      },
      FileExtension.MP3: {
        'format': 'bestaudio/best',
        'postprocessors': [{
          'key': 'FFmpegExtractAudio',
          'preferredcodec': 'mp3',
          'preferredquality': '192',
        }],
        'outtmpl': os.path.join(path , '%(title)s.%(ext)s'),
        'noplaylist': not is_playlist,
      }
    }

    return types[file_extension]
