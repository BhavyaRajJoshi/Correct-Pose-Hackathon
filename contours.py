import cv2 as cv 
import numpy as np 


img = cv.imread('Photos/pexels-eberhard-grossgasteiger-1398195.jpg')
cv.imshow('original image', img)

blank = np.zeros(img.shape, dtype= 'uint8')
cv.imshow('blank image', blank)

grayScaleImage = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Grayscale image', grayScaleImage)

cannyEdges = cv.Canny(img, 125, 175)
cv.imshow("cANNY Edges", cannyEdges )

contoursOfImage, hierarchies = cv.findContours(cannyEdges, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contoursOfImage)} contours found!!')

cv.drawContours(blank, contoursOfImage, -1, (0,0,255), 1)
cv.imshow("Contours drawn", blank)


cv.waitKey(0)