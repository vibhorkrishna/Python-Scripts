import subprocess

video = input("Enter the name of the video file: ")
new_resolution = input("Enter the new Resolution of the video you want: ")
bit_video = input("Enter the bitrate of video stream: ")
bit_audio = input("Enter the bitrate of audio stream: ")

subprocess.run(["ffmpeg", "-i", video, "-s", new_resolution, "-b:v", bit_video, "-b:a", bit_audio, 'output.mp4'])