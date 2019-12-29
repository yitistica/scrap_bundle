import youtube_dl

YDL_OPTS = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}


def download_youtube(urls: list, mp3_only=False):
    if mp3_only:
        with youtube_dl.YoutubeDL(YDL_OPTS) as ydl:
            ydl.download(urls)
    else:
        with youtube_dl.YoutubeDL() as ydl:
            ydl.download(urls)

