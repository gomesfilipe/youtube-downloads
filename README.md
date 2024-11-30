# Youtube Video Downloader

This repository contains the following features:

1. [Download Video as MP4](#vmp4)
2. [Download Video as MP3](#vmp3)
3. [Download Playlist as MP4](#pmp4)
4. [Download Playlist as MP3](#pmp3)

# Technologies

*Programming Language:*

```
Python 3.10.6
```

*Libraries*

```
pytube 15.0.0
yt-dlp 2024.11.18
```

# How to Use
- Clone this repository locally;

- Install libraries:

```bash
$ pip install pytube
$ pip install yt-dlp
```

- You can install using requirements.txt as well:

```bash
$ pip install -r requirements.txt
```

- Run script ```main.py``` using the flags.

```bash
$ main.py -l {LINK} -p {IS_PLAYLIST} -a {ONLY_AUDIO} -d {DIRECTORY}
```

- **LINK** - Link of video or playlist;
- **IS_PLAYLIST** - If link is playlist or not. Accepted values are "y" or "n". Defaults to "n";
- **ONLY_AUDIO** - If download must be as mp3. Accepted values are "y" or "n". Defaults to "n";
- **DIRECTORY** - Path to save downloaded audios or videos. Defaults to **"/downloads"**.

# Examples

<div id="vmp4"/>

## 1. Download Video as MP4
```
python3 main.py -l "https://www.youtube.com/watch?v=ff8UwvPK0G4&ab_channel=vkgoeswild" -p n -a n -d downloads
```

<div id='vmp3'/>

## 2. Download Video as MP3
```
python3 main.py -l "https://www.youtube.com/watch?v=ff8UwvPK0G4&ab_channel=vkgoeswild" -p n -a y -d downloads
```
<div id='pmp4'/>

## 3. Download Playlist as MP4
```
python3 main.py -l "https://www.youtube.com/playlist?list=PLS0vbAcrcuiXONnlAuD5n3urOwY1foq8n" -p y -a n -d downloads
```
<div id='pmp3'/>

## 4. Download Playlist as MP3
```
python3 main.py -l "https://www.youtube.com/playlist?list=PLS0vbAcrcuiXONnlAuD5n3urOwY1foq8n" -p y -a y -d downloads
```

# Info about Flags
```bash
$ python3 main.py -h
```


# Video Explanation

<a href="https://www.youtube.com/watch?v=lzCn83Mq9os&ab_channel=FilipeGomes">Click here</a> to watch a demonstration of use this project.