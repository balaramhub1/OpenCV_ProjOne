'''
Script to demonstrate image annotation using OpenCV

Syntax for creating a Rectangle on image:
cv2.rectangle(image, point1, point2, color, thickness, lineType )

Syntax for adding text to image:
cv2.text
'''

import cv2
import sys

img = cv2.imread("../resources/sample_images/landscape_img2.jpg")

if img is None:
    sys.exit("Image not found")

# create a duplicate copy of the image
imgCopy = img.copy()


# Draw a rectangle over the image
cv2.rectangle(imgCopy,(300,300),(400,450),(200,60,20), thickness= 5, lineType=cv2.LINE_AA)

cv2.imshow("image with rectangle",imgCopy)

# Adding text to an image
text = "Hello Everyone, how are you doing today, its a pleasant day!!"
cv2.putText(imgCopy,text,(200,200),cv2.FONT_HERSHEY_PLAIN,1.5,(190,0,10),thickness=2,lineType=cv2.LINE_AA)

cv2.imshow("with text", imgCopy)

cv2.waitKey(0)
cv2.destroyAllWindows()