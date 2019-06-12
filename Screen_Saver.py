#!/usr/bin/env python
# coding: utf-8

# In[1]:


# A screen Saver Project 
#Importing the Libraries
import numpy as np
import cv2


# In[2]:


def screensaver():
    canvas = np.zeros((480,680,3),dtype='uint8')
    dx=1
    dy=1
    x=100
    y=100
    while True:
        cv2.imshow('a',canvas)
        k=cv2.waitKey(10)
        canvas = np.zeros((480,680,3),dtype='uint8')
        x=x+dx
        y=y+dy
        cv2.circle(canvas,(x,y),25,(255,125,65),-1)
        if k!=-1:
            break
        if y >=480:
            dy *= -1
        elif y<=0:
            dy *= -1
        if x >=640:
            dx *= -1
        elif x<=0:
            dx *= -1
            

        


# In[5]:


#Background image
img1=cv2.imread("cat.jpeg")
while True:
    cv2.imshow('a',img1)
    k=cv2.waitKey(10000)
    if k==-1:
        screensaver()
    else:
        break
        


# In[ ]:




