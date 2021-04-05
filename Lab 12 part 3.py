import numpy as np
import cv2 as cv # this line imports the library with a nickname
import sys # imports library

img1 = cv.imread('BadFriends.jpeg')
img2 = cv.imread('2B1C.jpeg')
img2_2 = cv.resize(img2, (img1.shape[1], img1.shape[0]))

alpha = 0.2
dst = cv.addWeighted(img1, 1-alpha, img2_2, alpha, 0)
cv.imshow('dst',dst)
# print(img1.shape)
# print(img2.shape)
# print(img2_2.shape)
cv.waitKey(0)
cv.destroyAllWindows()

#this program is good for photoshopping or graphic designing