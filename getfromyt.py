from yt_dlp import YoutubeDL
 
def getfromyt(i):
    download_path = '~/Downloads/%(title)s.%(ext)s' #edit download folder
    ydl_opts = {'extract_flat': 'discard_in_playlist',
    'final_ext': 'mp3',
    'format': 'bestaudio/best',
    'fragment_retries': 10,
    'ignoreerrors': 'only_download', 
    'outtmpl': {'default': download_path}, 
    'postprocessors': [{'key': 'FFmpegExtractAudio',
                        'nopostoverwrites': False,
                        'preferredcodec': 'mp3',
                        'preferredquality': '5'},
                        {'key': 'FFmpegConcat',
                        'only_multi_video': True,
                        'when': 'playlist'}],
    'retries': 10,
    'warn_when_outdated': True}
 
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([i])
