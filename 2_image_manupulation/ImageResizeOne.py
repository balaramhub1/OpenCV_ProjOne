'''
Script to demonstrate image resizing using OpenCV
'''

import cv2
import sys

img = cv2.imread("../resources/sample_images/New_Zealand_Boat.jpg",cv2.IMREAD_COLOR)

if img is None:
    sys.exit("Image could not be loaded")

# crop the boat
boatImg = img[200:350, 400:500]
cv2.imshow("boat image", boatImg)

# resize the boat image
resizedImg = cv2.resize(boatImg, dsize = (200,300))
cv2.imshow("resized boat image", resizedImg)

# resize the boat image
dim = (300,400)
resizedImg2 = cv2.resize(boatImg, dim)
cv2.imshow("resized boat image again", resizedImg2)
# resizedImg = cv2.resize(boatImg, dsize = None, fx = 2, fy = 2, interpolation = None)

cv2.waitKey(0)
cv2.destroyAllWindows()