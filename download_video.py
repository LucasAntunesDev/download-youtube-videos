import os 
from pytube import YouTube

def download_video(url, destination_dir = 'videos'):

    youtube = YouTube(url)

    video_stream = youtube.streams.get_highest_resolution()

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    print(f'📥 Downloading "{youtube.title}"')
    video_stream.download(destination_dir)
    print('✅ Download finished')

url = input('🎬 Enter with the video URL: ')
download_video(url)