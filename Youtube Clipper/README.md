#Youtube Clipper
##Installing Dependencies:
Install 2 packages: ffmpeg and youtube_dl
For youtube_dl type the following command in terminal:
'''cmd
pip install youtube_dl
'''
For ffmpeg install it according to your OS

After installing them check whether both of them have been installed correctly by just typing 'ffmpeg' and 'youtube_dl' on terminal

#Steps to download the video
* Run the script '''cmd youtube_clip.py''' on terminal
'''cmd
python youtube_clip.py
'''
* After executing the script you will be asked for the link of the video, start time of the clip, end time of the clip and name of the output video
First you will be asked about the link of the youtube video you want to download as shown below:
'''cmd
Enter the Youtube video link:
'''
Example Input
'''cmd
Enter the Youtube video link: https://www.youtube.com/watch?v=hlWiI4xVXKY&ab_channel=SoothingRelaxation
'''
Now you will be asked to enter the start time of your video clip as shown below:
'''cmd
Enter start time of the video clip in HH:MM:SS|H:MM:SS|MM:SS|M:SS|SS|S format:
'''
Example Input
'''cmd
Enter start time of the video clip in HH:MM:SS|H:MM:SS|MM:SS|M:SS|SS|S format: 1:23
'''
Now you will be asked to enter the end time of your video clip as shown below:
'''cmd
Enter end time of the video clip in HH:MM:SS|H:MM:SS|MM:SS|M:SS|SS|S format:
'''
Example Input
'''cmd
Enter end time of the video clip in HH:MM:SS|H:MM:SS|MM:SS|M:SS|SS|S format: 1:23:45
'''
Then you will be asked to name your output video file as shown below:
'''cmd
Enter your output video name:
'''
Example Input
'''cmd
Enter your output video name: Relaxing_Video
'''
* Now your youtube video will be downloaded

##Note: This script works only for videos with mp4 format as most of the youtube video have that link
