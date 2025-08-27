'''
Script to demonstrate image annotation using OpenCV and draw a line on the image
syntax gpt Line:
cv2.line(image, point1, point2, color, thickness, lineType)
mandatory: image, point1 (x,y coordinate of point 1), point2(x,y coordinate of point 2 )

syntax for Circle:
cv2.circle(iamge, point, radius, color, thickness, lineType )

'''

import cv2
import sys

img = cv2.imread("../resources/sample_images/landscape_img1.jpg",1)

if img is None:
    sys.exit("Image not found")

cv2.imshow("original image",img)

# create a copy of the image
imgCopy = img.copy()

cv2.line(imgCopy,(450,400),(700,600),(100,120,216), thickness = 10, lineType=cv2.LINE_AA)

# Display the image with line
cv2.imshow("Image with Line", imgCopy)

# Draw a Cricle on the image
cv2.circle(imgCopy,(650,300),50,(20,40,80),thickness=5,lineType=cv2.LINE_4)

cv2.imshow("Image with Circle",imgCopy)

cv2.waitKey(0)
cv2.destroyAllWindows()