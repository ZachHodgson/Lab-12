import cv2 as cv # this line imports the library with a nickname
import sys # imports library
img = cv.imread('BadFriends.jpeg') # searches file for the BadFriends.jpeg image and saves to a variable
if img is None:
    sys.exit("The image could not be read.") # if this image can't be found the program will 
cv.imshow("OpenCV Image", img) # opens a window titles OpenCV Image, and displays the BadFriends.jpeg image

cv.waitKey(0) # closes the window when '0' is pressed
cv.destroyAllWindows() # destroys the app