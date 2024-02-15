import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("Photos/pexels-andrea-piacquadio-937690.jpg")
cv.imshow("original image", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("grayscale", gray)

##laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("laplacian", lap)

#SOBEL
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('sobel', combined_sobel)

#canny

canny = cv.Canny(gray, 150,175)
cv.imshow("canny", canny)

cv.waitKey(0)