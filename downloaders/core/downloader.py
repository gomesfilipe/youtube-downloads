from abc import ABC, abstractmethod

class Downloader(ABC):
  @abstractmethod
  def download_video(video_link: str, path: str) -> bool:
    pass

  @abstractmethod
  def download_audio(video_link: str, path: str) -> bool:
    pass

  @abstractmethod
  def download_video_playlist(playlist_link: str, path: str) -> bool:
    pass

  @abstractmethod
  def download_audio_playlist(playlist_link: str, path: str) -> bool:
    pass
