# Youtube Download Scripts

Este repositório contém scripts com o propósito de fazer downloads de:

1. [Vídeos do Youtube em formato mp4](#vmp4)
2. [Vídeos do Youtube em formato mp3](#vmp3)
3. [Playlists do Youtube em formato mp4](#pmp4)
4. [Playlists do Youtube em formato mp3](#pmp3)

# Tecnologias utilizadas

*Linguagem de programação:*

```
Python 3.10.6
```

*Módulo para efetuar download dos vídeos e playlists:*

```
pytube 12.1.2
```

# Como usar

Execute os seguintes passos para usar os scripts:

- Clone este repositório em sua máquina;

- Instale o módulo pytube com o comando abaixo:

```
pip install pytube
```

Para cada uma das funcionalidades **1**, **2**, **3** e **4** temos um arquivo associado. Assim, segue abaixo comandos para cada uma delas:

<div id="vmp4"/>

## 1. Download de vídeo em formato mp4

*Comando:*
```
python3 video_mp4.py "LINK_DO_VÍDEO"
```

*Exemplo:*
```
python3 video_mp4.py "https://www.youtube.com/watch?v=ff8UwvPK0G4&ab_channel=vkgoeswild"
```

<div id='vmp3'/>

## 2. Download de vídeo em formato mp3

*Comando:*
```
python3 video_mp3.py "LINK_DO_VÍDEO"
```

*Exemplo:*
```
python3 video_mp3.py "https://www.youtube.com/watch?v=ff8UwvPK0G4&ab_channel=vkgoeswild"
```

<div id='pmp4'/>

## 3. Download de playlist em formato mp4

*Comando:*
```
python3 playlist_mp4.py "LINK_DO_VÍDEO"
```

*Exemplo:*
```
python3 playlist_mp4.py "https://www.youtube.com/playlist?list=PLS0vbAcrcuiXONnlAuD5n3urOwY1foq8n"
```

<div id='pmp3'/>

## 4. Download de playlist em formato mp3

*Comando:*
```
python3 playlist_mp3.py "LINK_DO_VÍDEO"
```

*Exemplo:*
```
python3 playlist_mp3.py "https://www.youtube.com/playlist?list=PLS0vbAcrcuiXONnlAuD5n3urOwY1foq8n"
```

## Observações:

- De preferência, coloque o link do vídeo ou playlist entre aspas, como foi indicado acima. Se não colocar funcionará da mesma forma, contudo, se o link possuir o caractere **"&"**, o comando será executado em background.

- Os arquivos em formato **mp4** serão direcionados para a pasta **mp4-downloads**, que será criada automaticamente caso não exista.

- Os arquivos em formato **mp3** serão direcionados para a pasta **mp3-downloads**, que será criada automaticamente caso não exista.

# Breve demonstração de uso:

<a href="https://www.youtube.com/watch?v=lzCn83Mq9os&ab_channel=FilipeGomes">Clique aqui</a> para ver breve demonstração do uso dos scripts em vídeo.