import cv2

image = input("Enter the image name with extension: ")
img = cv2.imread(image, cv2.IMREAD_UNCHANGED)
 
print("Choose from 2 options:")
print("1. Manually choose height and width of image")
print("2. Equally scale the image")
option = input("Enter 1 or 2: ")
option = int(option)
if option == 2:
    scale_percent = input("Enter the scale percentage: ") # percent of original size
    scale_percent = int(scale_percent)
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
else:
    width = input("Enter width of image: ")
    height = input("Enter height of image: ")
width = int(width)
height = int(height)
dim = (width, height)
# resize image
print('Original Dimensions : ',img.shape)
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions : ',resized.shape)

cv2.imwrite('Output.PNG', resized)
#cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()