'''
Script to modify image pixel
'''
import cv2
import sys

img = cv2.imread("../resources/sample_images/checkerboard_18x18.png",cv2.IMREAD_COLOR)

if img is None:
    sys.exit("Not able to read image")

print(img)
cv2.imshow("original image", img)

print("First pixel value of image is : ", img[0, 0])
print("First pixel value of image is : ", img[0, 6])

# Creating a copy of the image for modification
copiedImg = img.copy()
cv2.imshow("duplicate image", copiedImg)

copiedImg[2, 2] = 200
copiedImg[2, 3] = 200
copiedImg[3, 2] = 200
copiedImg[3, 3] = 200

cv2.imshow("pixel modified image", copiedImg)
print(copiedImg)

cv2.waitKey(0)
cv2.destroyAllWindows()

