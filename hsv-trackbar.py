'''
This was build for Hand Gesture Assistant to deferentiate hand from the backgroud.
It will give you the HSV trackbar, Normal Camera and HSV output.

Input - The video stream from the camera.

Output - The window containg the colors with our given colour bounds.
    a. Tracking window with lower and upper bound of variables of HSV
    b. The original video stream from the camera.
    c. The video after masking with out inputs of uppper and lower bounds.

'''

import cv2
import numpy as np

def nothing(x):
    pass

#Getting the video input from the default web-camera
cap = cv2.VideoCapture(0)

#Creating a Trackbar window
cv2.namedWindow("Tracking")
cv2.createTrackbar("LH","Tracking",0,255,nothing)
cv2.createTrackbar("LS","Tracking",0,255,nothing)
cv2.createTrackbar("LV","Tracking",0,255,nothing)
cv2.createTrackbar("UH","Tracking",255,255,nothing)
cv2.createTrackbar("US","Tracking",255,255,nothing)
cv2.createTrackbar("UV","Tracking",255,255,nothing)

while True:
    _,frame=cap.read()

    '''
    BGR to HSV(Hue Saturation Value) color model
    Hue - All colors are represented in a 360 degree angle.
    Saturation - The amount of that color present.
    Value - The brightness of the color.
    '''
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #Our required shade of our will be a range.
    #Thus we have to use Lower bound and Upper bound to define our required color.

    #Variables that are used in the tracking window
    lh=cv2.getTrackbarPos("LH","Tracking")
    ls=cv2.getTrackbarPos("LS","Tracking")
    lv=cv2.getTrackbarPos("LV","Tracking")
    uh=cv2.getTrackbarPos("UH","Tracking")
    us=cv2.getTrackbarPos("US","Tracking")
    uv=cv2.getTrackbarPos("UV","Tracking")

    #The tracking window values to get the range.
    l_b=np.array((lh,ls,lv))
    u_b=np.array((uh,us,uv))

    #Masking our HSV image with our given bounds.
    mask=cv2.inRange(hsv,l_b,u_b)
    res=cv2.bitwise_and(frame,frame,mask=mask)

    #This will display two windows containg the original and after masking.
    cv2.imshow('img',frame)
    cv2.imshow('res',res)

    #Code will get terminated by pressing 'q'
    k= cv2.waitKey(1) & 0xFF
    if k==ord('q'):
        break

cap.release()  
cv2.destroyAllWindows()