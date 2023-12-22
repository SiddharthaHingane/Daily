from pytube import YouTube
video = '# your YT video link here'
yt = YouTube(video)
yt.streams.first().download()
print(f"Downloaded Video:{yt.title}")
