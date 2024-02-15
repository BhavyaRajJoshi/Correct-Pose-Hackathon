import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("Photos/pexels-julius-silver-753639.jpg")
cv.imshow("original image", img)
print(img.shape)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow("blank image", blank)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2),400,255,-1)
cv.imshow("mask", mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("masked image", masked)

cv.waitKey(0)
