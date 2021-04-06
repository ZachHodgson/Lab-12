#camera wasn't working, problem with revieving frame
import numpy as np
import cv2 as cv # this line imports the library with a nickname
import sys # imports library

cap = cv.VideoCapture(-1)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't recieve frame (stream end?). Exiting ...")
        break
    # our operations on the fram come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    # Display the resulting frame
    cv.imshow('frame', gray)
    
    if cv.waitKey(1)==ord('q'):
        break
    #when everything done, release the capture
    cap.release()
    cv.destroyAllWindows()