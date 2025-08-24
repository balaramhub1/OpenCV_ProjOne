'''
Script to demonstrate image cropping using OpenCV
'''

import cv2
import sys

img = cv2.imread("../resources/sample_images/New_Zealand_Boat.jpg",cv2.IMREAD_COLOR)

if img is None:
    sys.exit("Image could not be loaded")

'''
cv2.imshow("original image", img)
print("Shape of image : ", img.shape)
print("Size of image : ", img.size)

'''
# copy the image for cropping
imgCopy = img.copy()
cv2.imshow("duplicate img", imgCopy)

# crop the image
croppedImg = imgCopy[000:600, 000:903]
cv2.imshow("cropped img 1", croppedImg)

# crop the image
croppedImg2 = imgCopy[200:600, 300:903]
cv2.imshow("cropped img 2", croppedImg2)

# crop the image
croppedImg3 = imgCopy[300:600, 300:903]
cv2.imshow("cropped img 3", croppedImg3)

# crop the boat
boatImg = imgCopy[200:350, 400:500]
cv2.imshow("boat image", boatImg)

cv2.waitKey(0)
cv2.destroyAllWindows()