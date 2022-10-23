from turtle import title
from pytube import Playlist

link = input("enter the url playlist: ")

yt_Playlist = Playlist(link)


for video in yt_Playlist.videos:
    video.streams.get_highest_resolution().download("F:\Dj-python\Dev\Python basic\Traning")
    print("video Downloaded: ",video.title)

print("all video download")  