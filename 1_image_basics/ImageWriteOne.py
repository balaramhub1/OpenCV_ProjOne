'''
Script to open and image and write it

'''
import sys

import cv2


image1 = cv2.imread("../resources/sample_images/tom_cruise2.jpg")
# image1 = cv2.imread("../resources/sample_images/tom_cruise2.jpg", cv2.IMREAD_COLOR_RGB)

# Print the image data in Matrix format
print(image1)

cv2.imshow("image windows",image1)

if image1 is None:
    sys.exit("No such image ")

# Modify the color of the image
image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2HSV)
cv2.imshow("image with updated color",image2)

commandResponse = cv2.waitKey(0)

# Save the modified image, if user enters 's'
if commandResponse == ord('s'):
    cv2.imwrite("anotherImage.jpg",image2)