#out = cv2.VideoWriter("123.avi", fourcc, 30.0, (SCREEN_SIZE))#if keyboard.is_pressed('q'):#            break#b0 = Button(frame2,text='stop recording',command=stoprecord)#b0.pack(side='right')
###########
# remove flag as not required
#############
##def stoprecord():
##    print("stoprecord")
##    flag = 0
    
flag = True
def printtext():
    global e
    string = e.get() 
    #print(string)
    global out
    #out = cv2.VideoWriter("123.avi", fourcc, 30.0, (SCREEN_SIZE))
    out = cv2.VideoWriter(string+".avi", fourcc, 10.0, (SCREEN_SIZE))

def stoprecord():
    print("stoprecord")
    global flag
    flag = False
    #sleep(3)

def continuerecord():
    if flag:
        # make a screenshot
        img = pyautogui.screenshot()
        # convert these pixels to a proper numpy array to work with OpenCV
        frame = np.array(img)
        # convert colors from BGR to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # write the frame
        out.write(frame)
        # show the frame
        #cv2.imshow("screenshot", frame)
        #cv2.imshow(frame)
        # if the user clicks q, it exits
        #if keyboard.is_pressed('q'):
         #   break
        #if (flag == 0):
         #   break
    root.after(100,continuerecord)
    
def startrecord():
    print("startrecord")
    global flag
    flag = True
    continuerecord()
    
def close():
    print("close")
    cv2.destroyAllWindows()
    out.release()
    root.quit
    

    
    

from tkinter import *
from tkinter import ttk 
from tkinter.messagebox import askyesno 
import cv2
import numpy as np
import pyautogui
import keyboard
import time



SCREEN_SIZE = (1920, 1080)
fourcc = cv2.VideoWriter_fourcc(*"MJPG")

root = Tk()
root.title('Screen Recorder')
frame1 = Frame(root)
frame1.config(width = 100,bd = 5)
frame1.config(highlightbackground = "black")
frame1.pack()
frame2 = Frame(root,width = 2500,bd = 5)
frame2.pack()
frame3 = Frame(root, width = 100,bd = 5)
frame3.pack()
frame4 = Frame(root, width = 250,bd = 5)
frame4.pack()
#style = ttk.Style() 
#style.configure('TEntry', foreground = 'green') 
#Label (root , text = 'File Name').grid(row = 0)
l = Label(frame1 , text = 'File Name')
l.pack()

e = Entry(frame1)
e.pack()
e.focus_set()

b = Button(frame1,text='save file name',command=printtext)
b.pack(side='bottom')
b0 = Button(frame2,text='stop recording',command=stoprecord)
b0.pack(side='right')
#b0 = Label(frame2,text='press ESC\n to stop recording')
#b0.pack(side='left')
b1 = Button(frame2,text='start recording',command=startrecord)
b1.pack(side='left')
be = Button(frame3,text='EXIT',fg='red',command=root.quit)
be.pack(side='bottom')

contactlabel = Message(frame4,text = 'developed by Shreyas \ncontact :incredibletech11@gmail.com')
contactlabel.config(width = 250)
#contactlabel.config(length = 20)
contactlabel.pack(side = 'bottom')
root.mainloop()

