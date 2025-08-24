'''
Script to demonstrate how to reverse the color channels of an image
and how to split it into R, G, B channel images
'''

import cv2
import sys

# read image as original from the provided path
img = cv2.imread("../resources/sample_images/tom_cruise2.jpg")

img2 = cv2.imread("../resources/sample_images/landscape_img1.jpg")

if img is None:
    sys.exit("Not able to load image")

# display the read image in a new window
print("Display the image")
cv2.imshow("image view1",img)


# reverse the color for the image
print("Display the image after reversing the colors")
imgRev = img[:,:,::-1]
cv2.imshow("image view2",imgRev)

print("Displaying original landscape image")
cv2.imshow("landscape",img2)
# Split the image into 3 channels R, G, B
b, g, r = cv2.split(img)
print("Display the different channel images")
cv2.imshow("Blue channel image : ",b)

cv2.imshow("Green channel image : ",g)

cv2.imshow("Red channel image : ",r)

# Again merging images of above 3 channels
print("Merging the individual channel images into one")
imgMerged = cv2.merge((g, r, b))
cv2.imshow("merged image",imgMerged)
# wait for user input to exit window
cv2.waitKey(0)
cv2.destroyAllWindows()