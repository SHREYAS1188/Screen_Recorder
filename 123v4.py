# img = pyautogui.screenshot()
#cv2.imshow("screenshot", frame)


#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
import numpy as np
import pyautogui


# In[3]:
#print(pyautogui.size())


# In[4]:


SCREEN_SIZE = (1920, 1080)
fourcc = cv2.VideoWriter_fourcc(*"MJPG")
# change output name
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (SCREEN_SIZE))


# In[6]:


while True:
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
    # if the user clicks q, it exits
    if cv2.waitKey(1) == ord("q"):
        break

# make sure everything is closed when exited
cv2.destroyAllWindows()
out.release()


# In[ ]:




