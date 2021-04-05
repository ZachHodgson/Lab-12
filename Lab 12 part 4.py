import numpy as np
import cv2 as cv # this line imports the library with a nickname
import sys # imports library

img = cv.imread("BadFriends.jpeg")
res = cv.resize(img,None,fx=0.5,fy=0.5,interpolation=cv.INTER_CUBIC)

cv.imwrite("Canny.jpeg",cv.Canny(res,200,300))# Canny in one line
cv.imshow("Canny.jpeg",cv.imread("Canny.jpeg"))
cv.waitKey(0)
cv.destroyAllWindows()

#This program could also be used for graphic design