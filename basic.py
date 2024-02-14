import cv2 as cv  

img = cv.imread('Photos/pexels-andrea-piacquadio-937690.jpg')
cv.imshow('original image', img)

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale image', gray_img)

#BLURRING THE IMAGE
##Edge detection

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny edges', canny)

##dilating the image

dilated = cv.dilate(canny, (3,3), iterations = 1)
cv.imshow('Dilated image', dilated)

cv.waitKey(0)