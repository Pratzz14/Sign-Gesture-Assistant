'''
Dataset Creator for Sign Gesture Recognition
'''
'''
Input - 
    if q is pressed - Terminate the program.
    if c is pressed - Capture the image 
    where the background is black 
    the hand should be white 
    the reflection of white light might be problematic
'''

import os
import cv2
import numpy as np

#Fix the directory
directory = r'D:\Computer Vision\Sign Gesture Assistant\Yes_No_Classifier\Dataset\testing'
os.chdir(directory) 

#Input from the web camera
cap = cv2.VideoCapture(0)

#Variable used while writing the image.
i=0 

# These lower and upper bounds are there to calculate the hsv color of the hand.
l_b=np.array((0,56,0)) 
u_b=np.array((255,255,255))

while(True):
    ret, frame = cap.read()

    #To adjust yourself in the camera
    cv2.imshow("imshow",frame)
    key=cv2.waitKey(30)

    #If 'q' pressed quit the program.
    if key==ord('q'):
        break

    #If 'c' pressed then capture.
    if key==ord('c'):

        #BGR to HSV
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

        #Masking the image and applying bitwise_and operator.
        mask=cv2.inRange(hsv,l_b,u_b)
        frame=cv2.bitwise_and(frame,frame,mask=mask)

        #Gray Scaling the image.
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #Applying Gaussian Blur with kernel of 9*9
        frame = cv2.GaussianBlur(frame, (9, 9), 0)

        #Applying Thresholding.
        ret,frame = cv2.threshold(frame,25,255,cv2.THRESH_BINARY)

        cv2.imshow("imshow2",frame)

        #Save the hsv image with the file name.
        i+=1
        filename = str(i)+'p.png'
        print(filename)
        cv2.imwrite(filename, frame)

# release the capture
cap.release()
cv2.destroyAllWindows()
