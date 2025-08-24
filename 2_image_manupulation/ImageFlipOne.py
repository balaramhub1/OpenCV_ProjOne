'''
Script to demonstrate flipping of an image using OpenCV
'''
import cv2
import sys

img = cv2.imread("../resources/sample_images/landscape_img1.jpg", cv2.IMREAD_COLOR)

if img is None:
    sys.exit("Image not found")

# show image
cv2.imshow("original image", img)

# flip the image
flipImg1 = cv2.flip(img,0)
cv2.imshow("flipped 1 image", flipImg1)

flipImg2 = cv2.flip(img,1)
cv2.imshow("flipped 2 image", flipImg2)

flipImg3 = cv2.flip(img, -1)
cv2.imshow("flipped 3 image", flipImg3)


cv2.waitKey(0)
cv2.destroyAllWindows()
