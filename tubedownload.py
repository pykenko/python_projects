#!/usr/bin/env python
#from pytube import YouTube
import sys
import os
from pytubefix import YouTube
from pytubefix.cli import on_progress

#**Usage Notes:**
#Make sure you downloaded pytubefix before using this tool
#if you havent you can use "pip install pytubefix"

download_directory = "Downloaded_video"

if not os.path.exists(download_directory):
    os.makedirs(download_directory)

if len(sys.argv) != 2:
    print(f"How to use : ./tubedownload <URL>")
else:
    user_link = sys.argv[1]
    print("  __       ___.           ")
    print("_/  |_ __ _\\_ |__   ____  ")
    print("\\   __\\  |  \\ __ \\_/ __ \\ ")
    print(" |  | |  |  / \\_\\ \\  ___/ ")
    print(" |__| |____/|___  /\\___  >")
    print("                \\/     \\/ ")
    try:
        video = YouTube(user_link)
        video_down = video.streams.get_highest_resolution()
        audio_down = video.streams.get_audio_only()
        print(f"\nFound Video {video.title}\n")
        print("Downloading video")
        video_down.download(output_path=download_directory,filename=f"{video.title}.mp4")

        print("Downloading sound")
        audio_down.download(output_path=download_directory,filename=f"{video.title}.mp3")

        print("\nFinished!")
    except Exception as a:
        print(f"Error processing URL '{user_link}': {a}")


    input("enter to exit")