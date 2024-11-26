import argparse
from enums.dual_option import DualOption
from downloaders.core.downloader import Downloader
from downloaders.yt_dlp_downloader import YtDlpDownloader
from typing import Dict, Callable

yes = DualOption.YES.value
no = DualOption.NO.value

valid_options_help = f'Valid values are "{yes}" ({DualOption.YES.to_str()}) or "{no}" ({DualOption.NO.to_str()}).'

def validate_option(value: str) -> str:
  if value not in DualOption.values():
    raise argparse.ArgumentTypeError(valid_options_help)

  return value

parser = argparse.ArgumentParser(description = 'Download Videos and Playlists from Youtube as MP3 or MP4.')

parser.add_argument(
  '-p',
  '--playlist',
  type = validate_option,
  default = DualOption.NO.value,
  help = f'Is Playlist? {valid_options_help}',
)

parser.add_argument(
  '-a',
  '--audio',
  type = validate_option,
  default = DualOption.NO.value,
  help = f'Only Audio? {valid_options_help}',
)

parser.add_argument(
  '-l',
  '--link',
  type = str,
  required = True,
  help = 'Video or Playlist Link.',
)

parser.add_argument(
  '-d',
  '--dir',
  type = str,
  required = False,
  default = 'downloads',
  help = 'Path to Save Video or Playlist',
)

args = parser.parse_args()
key = f'{args.playlist}{args.audio}'
downloader: Downloader = YtDlpDownloader()

inputs: Dict[str, Callable[[str, str], bool]] = {
  f'{yes}{yes}': lambda link, path: downloader.download_audio_playlist(link, path),
  f'{yes}{no}': lambda link, path: downloader.download_video_playlist(link, path),
  f'{no}{yes}': lambda link, path: downloader.download_audio(link, path),
  f'{no}{no}': lambda link, path: downloader.download_video(link, path),
}

inputs[key](args.link, args.dir)
