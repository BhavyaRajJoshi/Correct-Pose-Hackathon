import cv2 as cv 

#img = cv.imread('Photos/pexels-eberhard-grossgasteiger-1398195.jpg')

#cv.imshow('Cat', img)


capture = cv.VideoCapture(0,1)

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()


#cv.waitKey(0)