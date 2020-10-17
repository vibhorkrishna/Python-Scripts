# Image Resizer
Image Resizer resizes the image
## Installing the Libraries:
Install opencv by typing the following command in terminal:
```
pip install opencv-python
```
## Usage
Run the script ```Image_Resizer.py``` on terminal
```
python Image_Resizer.py
```
After executing the script you will be asked to enter the name of the image and how you want to resize the image.
#### Note: Make sure the the image is on the same directory as the python script

Sample Input:
```
Enter the image name with extension: sample_input.jpg
Choose from 2 options:
1. Manually choose height and width of image
2. Equally scale the image
Enter 1 or 2: 2
Enter the scale percentage: 50
```

![Alt text](https://github.com/vibhorkrishna/Python-Scripts/blob/main/Image%20Resizer/sample_input.jpg?raw=true)

Sample Output:

```
Original Dimensions :  (800, 800, 3)
Resized Dimensions :  (400, 400, 3)
```
![Alt text](https://github.com/vibhorkrishna/Python-Scripts/blob/main/Image%20Resizer/Output.PNG?raw=true)

#### Note: Your resized image will be saved on the same directory as the python script
