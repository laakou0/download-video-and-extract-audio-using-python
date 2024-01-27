from pytube import YouTube
import time
from moviepy.video.io.VideoFileClip import VideoFileClip

choise = input("Welcome to this programme. First, you want to download video from youtube or extract audio from video, video/audio : ")
if choise == "video":
    def YouTubevideo():
        # streams url
        url = input("Enter the url of the video: ")
        yt = YouTube(url)

        # Video Title
        print("Title: ", yt.title)

        # Video Description
        print("Description: ", yt.description)

        # Views
        print("views: ", yt.views)

        stream = yt.streams

        str = stream.get_highest_resolution()

        Download = str

        # print(Download)
        download = Download.download('/Users/NBH/Downloads')

        print(download)

        [print('-' * i, end='', flush=True) or time.sleep(1) for i in range(1, 6)]

        print("\nDownload complete")


    YouTubevideo()
if choise == "audio":
    def extract_audio(video_path, audio_path):
        video_clip = VideoFileClip(video_path)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(audio_path, codec='mp3')
        audio_clip.close()


    # Replace 'C:\Users\NBH\Desktop\bb.mp4' with the correct path to your video file
    # and 'C:\Users\NBH\Music\example_audio.mp3' with the desired output path and file name
    video_path = r'C:\Users\NBH\Desktop\bb.mp4'
    audio_path = r'C:\Users\NBH\Music\example_audio.mp3'

    extract_audio(video_path, audio_path)