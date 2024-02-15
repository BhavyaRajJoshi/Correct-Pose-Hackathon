import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("Photos/pexels-helena-lopes-2253275.jpg")
cv.imshow("original image", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY )
cv.imshow("grayscale", gray)

#grayscale histogram
gray_hist = cv.calcHist([gray], [0], None, [256], [0,256] )

plt.figure()
plt.title("grayscale histogram")
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

cv.waitKey(0)
