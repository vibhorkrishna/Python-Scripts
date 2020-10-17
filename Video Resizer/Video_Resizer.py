import subprocess

video = input("Enter the name of the video file: ")
new_resolution = input("Enter the new Resolution of the video you want: ")

subprocess.run(["ffmpeg", "-i", video, "-s", new_resolution, "-b:v", '4M', "-b:a", '2M', 'output.mp4'])