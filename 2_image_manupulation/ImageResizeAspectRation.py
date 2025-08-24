'''
Script to demonstrate image resizing while Maintaining Aspect Ratio
'''

import cv2
import sys

# read the image
img = cv2.imread("../resources/sample_images/New_Zealand_Boat.jpg",1)

if img is None:
    sys.exit("Image could not be loaded")

# Crop the boat image and create another image
boatImg = img[200:350, 400:500]

# show the image
cv2.imshow("original image", boatImg)

print("Shape of image : ", boatImg.shape)
print("Size of image : ", boatImg.size)

desiredWidth = 200
aspectRatio = desiredWidth/boatImg.shape[1]
desiredHeight = int(boatImg.shape[0] * aspectRatio)
newDim = (desiredWidth, desiredHeight)

print("Aspect Ratio : ", aspectRatio)
print("Width and Height are : ", desiredWidth, " , ", desiredHeight)

resizedBoat = cv2.resize(boatImg, newDim)
cv2.imshow("Resized boat and Maintained Aspect Ratio", resizedBoat)

cv2.waitKey(0)
cv2.destroyAllWindows()