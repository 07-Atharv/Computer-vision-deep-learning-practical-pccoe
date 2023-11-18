#!/usr/bin/env python
# coding: utf-8

# import cv2
# import numpy as np
# store = cv2.imread('C:/Users/ATHARV/Desktop/imgone.jpg')
# cv2.imshow('orignal',store)
# cv2.waitKey(0)

# In[12]:


Gaussian = cv2.GaussianBlur(store,(7,7),0)
cv2.imshow('Gaussian filter',Gaussian)
cv2.waitKey(0)
# dst = cv2.GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType=BORDER_DEFAULT]]] )


# In[10]:


median = cv2.medianBlur(store,5)
cv2.imshow('Median filter',median)
cv2.waitKey(0)


# ########## sobel_f = cv2.Sobel(store,cv2.COLOR_BGR2GRAY,1,0,3)
# #64 bit floating point bit
# cv2.imshow('Sobel Filter',sobel_f)
# cv2.waitKey(0)
# ########## Sobel(src_gray, grad_x, ddepth, 1, 0, ksize, scale, delta, BORDER_DEFAULT);
