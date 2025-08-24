'''

Script to demonstrate how to convert color of the image to other colors
'''

import cv2
import sys

#img = cv2.imread("../resources/sample_images/landscape_img2.jpg",cv2.COLOR_BGR2HLS)

#img = cv2.imread("../resources/sample_images/landscape_img2.jpg",cv2.IMREAD_COLOR)
img = cv2.imread("../resources/sample_images/landscape_img2.jpg") # same as above

#img = cv2.imread("../resources/sample_images/landscape_img2.jpg",cv2.IMREAD_GRAYSCALE)

if img is None:
    sys.exit("Image not found, exiting...")

print("Displaying the original image")
cv2.imshow("landscape",img)

img2 = cv2.cvtColor(img, cv2.COLOR_RGB2YCrCb)

cv2.imshow("changed color 1",img2)

# Another color space
img3 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # HSV - Hue (color) , Saturation (intensity of color) , Value (value)

cv2.imshow("changed color 2",img3)

# Split image by H, S, V
h, s, v = cv2.split(img3)

print("Image with Hue only : ")
cv2.imshow("Hue channel Image", h+20)

print("Image with Saturation only : ")
cv2.imshow("Saturation channel Image", s)

print("Image with Value only : ")
cv2.imshow("Value channel image", v)

# Merging above 3 channles into one
mergedImg = cv2.merge((h, s, v))
print("Merged Image  : ")
cv2.imshow("merged image", mergedImg)


cv2.waitKey(0)
cv2.destroyAllWindows()