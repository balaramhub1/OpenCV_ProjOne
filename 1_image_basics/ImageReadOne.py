'''
Script to read image using OpenCV
'''
import cv2
import sys

''' imread() takes 2 arguments
1 - absolute or relative file path
2 - read image in particular format like color/gray scale etc 
'''

img = cv2.imread("../resources/sample_images/tom_cruise1.jpg",1)

# print the image data in Matrix format
print(img)

print("Shape of the image")
print(img.shape)
print("Size of the image")
print(img.size)
print("Type of image")
print(img.dtype)

if img is None:
    sys.exit("Not able to load the image")


cv2.imshow("image window",img)

# press any key to quit the image window
cv2.waitKey(0)

cv2.destroyAllWindows()