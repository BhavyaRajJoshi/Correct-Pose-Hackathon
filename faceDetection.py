import cv2 as cv 
import numpy as np 

img = cv.imread('Photos/people.jpeg')
cv.imshow('original image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("grayscale", gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

print(f'number of faces found is : {len(faces_rect)}')

for(x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness = 2)

cv.imshow("detected face", img)

cv.waitKey(0)
