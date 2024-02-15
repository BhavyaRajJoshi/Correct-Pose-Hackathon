import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(),(30,30), (370,370),255,0)
circle = cv.circle(blank.copy(),(200,200),200,255,0)

#bitwise_and
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow("Bitwise and", bitwise_and)

#bitwise or

bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("bitwise or ", bitwise_or)

cv.imshow("rectangle ", rectangle)
cv.imshow("circle", circle)

cv.waitKey(0)