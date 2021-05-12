from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout,QRadioButton, QPushButton,QGridLayout,QHBoxLayout, QGroupBox
from PyQt5.QtGui import QPixmap
import sys
import cv2
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
import numpy as np
import PyQt5.QtGui as qtg 
import PyQt5.QtWidgets as qtw 
from PyQt5.QtCore import *
import time
import os
import HandTrackingModule as htm
from tkinter import *
import threading

text = "YO "
number=True
alphabet=False
sign=False

'''
Global fonts if we have to embedded text on OpenCV screen.
'''
font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (280,400)
fontScale              = 1
fontColor              = (255,255,255)
lineType               = 2

def check_number(img,lmList):
    '''
    Upon the position of the joints it predicts which number it is.

    Args:
        img : OpenCV image.
        lmList : Joint points position.
        fingers : List of which fingers is up.
        str_number : Text variable which is predicted.

    Availabe numbers : 0,1,2,3,4,5,6,7,8,9,10,50,100
    '''
    fingers=[]
    if len(lmList) != 0:
        fingers=[]

        #thumb
        if lmList[4][1] > lmList[2][1]:
            #print("0",end=" ")
            fingers.append(0)
        else:
            #print("Index DOWN")
            pass

        #index
        if lmList[8][2] < lmList[6][2]:
            #print("1",end=" ")
            fingers.append(1)
        else:
            #print("Index DOWN")
            pass

        #middle
        if lmList[12][2] < lmList[10][2]:
            #print("2",end=" ")
            fingers.append(2)
        else:
            #print("Index DOWN")
            pass
        
        #ring
        if lmList[16][2] < lmList[14][2]:
            #print("3",end=" ")
            fingers.append(3)
        else:
            #print("Index DOWN")
            pass

        #pinky
        if lmList[20][2] < lmList[18][2]:
            #print("4",end=" ")
            fingers.append(4)
        else:
            #print("Index DOWN")
            pass

    str_number = ""

    #zero
    zero=[0]
    if set(fingers)==set(zero):
        #print("ZERO")
        str_number = "ZERO"

    #one
    one=[1]
    if set(fingers)==set(one):
        #print("ZERO")
        str_number = "ONE"

    #two
    two=[1,2]
    if set(fingers)==set(two):
        #print("ZERO")
        str_number = "TWO"
    
    #three
    three=[0,1,2]
    if set(fingers)==set(three):
        #print("ZERO")
        str_number = "THREE"

    #four
    four=[1,2,3,4]
    if set(fingers)==set(four):
        #print("ZERO")
        str_number = "FOUR"
    
    #five
    five=[0,1,2,3,4]
    if set(fingers)==set(five):
        #print("ZERO")
        str_number = "FIVE"

    #six
    six=[1,2,3]
    if set(fingers)==set(six):
        #print("ZERO")
        str_number = "SIX"

    #seven
    seven=[1,2,4]
    if set(fingers)==set(seven):
        #print("ZERO")
        str_number = "SEVEN"

    #eight
    eight=[1,3,4]
    if set(fingers)==set(eight):
        #print("ZERO")
        str_number = "EIGHT"
    
    #nine
    nine=[2,3,4]
    if set(fingers)==set(nine):
        #print("ZERO")
        str_number = "NINE"

    #ten
    ten=[0,4]
    if set(fingers)==set(ten):
        #print("ZERO")
        str_number = "TEN"

    #fifty
    fifty=[0,3,4]
    if set(fingers)==set(fifty):
        #print("ZERO")
        str_number = "FIFTY"

    #hundred
    hundred=[0,2,3,4]
    if set(fingers)==set(hundred):
        #print("ZERO")
        str_number = "HUNDRED"
    

    return img,str_number
################################

#right_hand - check signs
def check_sign(img,lmList):
    '''
    Upon the position of the joints it predicts which sign it is.

    Args:
        img : OpenCV image.
        lmList : Joint points position.
        fingers : List of which fingers is up.
        str_number : Text variable which is predicted.

    Availabe Sign : Yes,No
                    Hello, Good Bye
                    Peace, Love
                    Correct, Tend to, you
    '''
    fingers=[]
    if len(lmList) != 0:
        fingers=[]

        #thumb
        if lmList[4][1] > lmList[2][1]:
            #print("0",end=" ")
            fingers.append(0)
        else:
            #print("Index DOWN")
            pass

        #index
        if lmList[8][2] < lmList[6][2]:
            #print("1",end=" ")
            fingers.append(1)
        else:
            #print("Index DOWN")
            pass

        #middle
        if lmList[12][2] < lmList[10][2]:
            #print("2",end=" ")
            fingers.append(2)
        else:
            #print("Index DOWN")
            pass
        
        #ring
        if lmList[16][2] < lmList[14][2]:
            #print("3",end=" ")
            fingers.append(3)
        else:
            #print("Index DOWN")
            pass

        #pinky
        if lmList[20][2] < lmList[18][2]:
            #print("4",end=" ")
            fingers.append(4)
        else:
            #print("Index DOWN")
            pass

    str_number = ""

    # #zero
    # zero=[0]
    # if set(fingers)==set(zero):
    #     #print("ZERO")
    #     str_number = "ZERO"

    
    
    #hello
    hello=[1,2,3,4]
    if set(fingers)==set(hello):
        #print("ZERO")
        str_number = "HELLO"
    
    #goodbye
    goodbye=[1,2,3]
    if set(fingers)==set(goodbye):
        #print("ZERO")
        str_number = "GOOD BYE"

    #correct
    correct=[2,3,4]
    if set(fingers)==set(correct):
        #print("ZERO")
        str_number = "CORRECT"

    #tento
    tento=[0,1,3,4]
    if set(fingers)==set(tento):
        #print("ZERO")
        str_number = "TEND TO"

    #you
    you=[0,4]
    if set(fingers)==set(you):
        #print("ZERO")
        str_number = "YOU"
    
    #yes
    yes=[0]
    if set(fingers)==set(yes):
        #print("ZERO")
        str_number = "YES"

    #no
    no=[0,1,2]
    if set(fingers)==set(no):
        #print("ZERO")
        str_number = "NO"
    
    #peace
    peace=[1,2]
    if set(fingers)==set(peace):
        #print("ZERO")
        str_number = "PEACE"

    #love
    love=[0,1]
    if set(fingers)==set(love):
        #print("ZERO")
        str_number = "LOVE"

    return img,str_number

#######################################

#right_hand - alphabet
def check_alphabet(img,lmList):
    '''
    Upon the position of the joints it predicts which alphabet it is.

    Args:
        img : OpenCV image.
        lmList : Joint points position.
        fingers : List of which fingers is up.
        str_number : Text variable which is predicted.

    Available alphabet: A,E,I,O,U
                        B,F,G,W
    '''
    fingers=[6]
    if len(lmList) != 0:
        fingers=[]

        #thumbx
        if lmList[4][1] > lmList[2][1]:
            #print("0",end=" ")
            fingers.append(0)
        else:
            #print("Index DOWN")
            pass

        #thumby
        if lmList[4][2] > lmList[2][2]:
            #print("0",end=" ")
            fingers.append(5)
        else:
            #print("Index DOWN")
            pass

        #index
        if lmList[8][2] < lmList[6][2]:
            #print("1",end=" ")
            fingers.append(1)
        else:
            #print("Index DOWN")
            pass

        #middle
        if lmList[12][2] < lmList[10][2]:
            #print("2",end=" ")
            fingers.append(2)
        else:
            #print("Index DOWN")
            pass
        
        #ring
        if lmList[16][2] < lmList[14][2]:
            #print("3",end=" ")
            fingers.append(3)
        else:
            #print("Index DOWN")
            pass

        #pinky
        if lmList[20][2] < lmList[18][2]:
            #print("4",end=" ")
            fingers.append(4)
        else:
            #print("Index DOWN")
            pass

    str_number = ""

    #A
    A=[0]
    if set(fingers)==set(A):
        #print("ZERO")
        str_number = "A"
        text = "A"
    
    #E
    E=[0,1,4]
    if set(fingers)==set(E):
        #print("ZERO")
        str_number = "E"
        #text = "E"

    #I
    I=[4]
    if set(fingers)==set(I):
        #print("ZERO")
        str_number = "I"
        #text = "I"
    
    #O
    O=[]
    if set(fingers)==set(O):
        #print("ZERO")
        str_number = "O"
        #text = "O"

    #U
    U=[1,2]
    if set(fingers)==set(U):
        #print("ZERO")
        str_number = "U"
        #text = "U"

    #B
    B=[1,2,3,4]
    if set(fingers)==set(B):
        #print("ZERO")
        str_number = "B"
        #text = "B"

    #F
    F=[2,3,4]
    if set(fingers)==set(F):
        #print("ZERO")
        str_number = "F"
        #text = "B"

    #G
    G=[1]
    if set(fingers)==set(G):
        #print("ZERO")
        str_number = "G"
        #text = "B"

    #W
    W=[1,2,3]
    if set(fingers)==set(W):
        #print("ZERO")
        str_number = "W"
        #text = "B"

    return img,str_number




class App(QWidget):
    '''
    This is the code for the GUI.
    The GUI has :
        - openCV updated image
        - The translated sign Text 
        - Three radio button
        - The warning text.
    '''
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sign Language Assistant")
        self.disply_width = 640
        self.display_height = 480
        self.image_label = QLabel(self)
        self.image_label.resize(self.disply_width, self.display_height)
        self.textLabel = QLabel('**Make sure that the background is not too noisy.**')

        vbox = QGridLayout()

        vbox.addWidget(self.image_label,0,0)
        vbox.addWidget(self.textLabel,1,0)
        # set the vbox layout as the widgets layout
        self.setLayout(vbox)

        # create the video capture thread
        self.thread = VideoThread()
        self.thread.change_pixmap_signal.connect(self.update_image)
        self.thread.start()

        self.my_label = qtw.QLabel(text)
        self.my_label.setFont(qtg.QFont('Helvetica',30))
        self.my_label.setAlignment(Qt.AlignCenter)
        self.layout().addWidget(self.my_label,2,0)

        self.dog = QRadioButton('Numbers')
        self.dog.setLayoutDirection(Qt.LeftToRight)
        self.dog.setChecked(True)
        self.cat = QRadioButton('Alphabets')
        self.sign = QRadioButton('Sign')
        
        vbox.addWidget(self.dog,0,1)
        vbox.addWidget(self.cat,0,2)
        vbox.addWidget(self.sign,0,3)

    def closeEvent(self, event):
        self.thread.stop()
        event.accept()


    @pyqtSlot(np.ndarray)
    def update_image(self, cv_img):
        """
        Updates the image_label with a new opencv image.

        As this regularly updates the image, I have made this loop also collect which radio button is choosed.
        If one of the botton is pressed the global variable is updated.

        """
        qt_img = self.convert_cv_qt(cv_img)
        self.image_label.setPixmap(qt_img)

        global number,alphabet,sign
        if self.dog.isChecked():
            number=True
            alphabet=False
            sign=False
            #print(sign)
        if self.cat.isChecked():
            number=False
            alphabet=True
            sign=False
            #print(sign)
        if self.sign.isChecked():
            number=False
            alphabet=False
            sign=True
            #print(sign)
    
    def convert_cv_qt(self, cv_img):
        """
        Convert from an opencv image to QPixmap
        """
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.KeepAspectRatio)
        self.my_label.setText(text)
        return QPixmap.fromImage(p)

    

class VideoThread(QThread):
    '''
    The video thread which contains the main loop of the OpenCV.
    '''
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def __init__(self):
        super().__init__()
        self._run_flag = True

    def run(self):
        '''
        Runs the OpenCV main while loop.
        global text : It was used to embedded text on the camera screen.
        cap : OpenCV video capture 0- USB camera

        ret : return true if image is found.
        cv_img : Reads the image frame. And find the hands.
        lmList : Contains the position of the joints.

        As we have three option to check numbers, alphabets and sign.
        Thus and if-else logic to call the appropriate function.


        '''
        global text
        # capture from web cam
        cap = cv2.VideoCapture(0)
        detector = htm.handDetector(detectionCon=0.75)
        #i=0
        while self._run_flag:
            ret, cv_img = cap.read()
            cv_img = detector.findHands(cv_img)
            lmList = detector.findPosition(cv_img, draw=False)

            fingers=[]

            if number:
                cv_img,text = check_number(cv_img,lmList)
            if alphabet:
                cv_img,text = check_alphabet(cv_img,lmList)
            if sign:
                cv_img,text = check_sign(cv_img,lmList)
            

            if ret:
                self.change_pixmap_signal.emit(cv_img)
            
            
        # shut down capture system
        cap.release()

    def stop(self):
        """
        Sets run flag to False and waits for thread to finish
        """
        self._run_flag = False
        self.wait()


    
if __name__=="__main__":
    app = QApplication(sys.argv)
    a = App()
    a.show()
    sys.exit(app.exec_())