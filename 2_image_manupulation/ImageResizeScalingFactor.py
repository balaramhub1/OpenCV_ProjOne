'''
Script to demonstrate image resizing using scaling factors, in OpenCV
'''

import cv2
import sys

# read an image
img = cv2.imread("../resources/sample_images/New_Zealand_Boat.jpg",cv2.IMREAD_COLOR)

if img is None:
    sys.exit("Image not found")

# crop the boat image
boatImg = img[200:350, 400:500]
cv2.imshow("boat image", boatImg)
print("Size before resizing is : ", boatImg.size)
print("Shape before resizing is : ", boatImg.shape)

# Resizing the cropped image using scaling factors
resizedImg = cv2.resize(boatImg,None,fx=2,fy=2)
cv2.imshow("resized boat image", resizedImg)
print("Size of after resizing is : ", resizedImg.size)
print("Shape before resizing is : ", resizedImg.shape)


cv2.waitKey(0)
cv2.destroyAllWindows()