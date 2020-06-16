from tkinter import *
from tkinter import ttk 
from tkinter.messagebox import askyesno 
import cv2
import numpy as np
import pyautogui
import keyboard
import time

flag = True
def printtext():
    global e
    string = e.get()
    global out
    out = cv2.VideoWriter("string.avi", fourcc, 10.0, (SCREEN_SIZE))


def stoprecord():
    print("stoprecord")
    global flag
    flag = False
    out.release()

def continuerecord():
    if flag:
        print("recording")
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
    root.after(20,continuerecord)
    
def startrecord():
    print("startrecord")
    global flag
    flag = True
    continuerecord()
    
def close():
    print("close")
    cv2.destroyAllWindows()
    root.quit
    

##


SCREEN_SIZE = (1920, 1080)
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')

root = Tk()
root.title('Screen Recorder')
frame1 = Frame(root)
frame1.config(width = 100,bd = 5)
frame1.pack()
frame2 = Frame(root,width = 2500,bd = 5)
frame2.pack()
frame3 = Frame(root, width = 100,bd = 5)
frame3.pack()
frame4 = Frame(root, width = 250,bd = 5)
frame4.pack()
l = Label(frame1 , text = 'File Name')
l.pack()

e = Entry(frame1)
e.pack()
e.focus_set()

b = Button(frame1,text='save file name',command=printtext)
b.pack(side='bottom')
b0 = Button(frame2,text='stop recording',command=stoprecord)
b0.pack(side='right')
b1 = Button(frame2,text='start recording',command=startrecord)
b1.pack(side='left')
be = Button(frame3,text='EXIT',fg='red',command=root.quit)
be.pack(side='bottom')

contactlabel = Message(frame4,text = 'developed by Shreyas \ncontact :incredibletech11@gmail.com')
contactlabel.config(width = 250)
contactlabel.pack(side = 'bottom')
root.mainloop()

