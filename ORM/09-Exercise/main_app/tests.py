from django.test import TestCase

# Create your tests here.

from pytube import YouTube

# yt_video = YouTube('https://www.youtube.com/watch?v=3HoPgqh8FSw&t=834s')
# file = yt_video.streams.get_audio_only()
# file.download('D:\Downloads')

YouTube('https://www.youtube.com/watch?v=3HoPgqh8FSw&t=834s').streams.get_audio_only().download('D:\Downloads')