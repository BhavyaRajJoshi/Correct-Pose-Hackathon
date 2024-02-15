import cv2 as cv
import matplotlib.pyplot as plt


img =cv.imread('Photos/mostafa-meraji-HJgEB78b2Z8-unsplash.jpg')
cv.imshow('Cat', img)

plt.imshow(img)
plt.show()


#bgr to grayscale
grayImage = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray scale image", grayImage)

#BGR to HSV
hsvImage = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV image", hsvImage)

# BGR TO LAB
labImage = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow("LAB IMAGE", labImage)

# BGR TO 

cv.waitKey(0)