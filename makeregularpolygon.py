# -*- coding: utf-8 -*-
"""MakeRegularPolygon.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12GVc9ogYJszrJbq332hdWfRKOu3dMv8o
"""

import cv2
import numpy as np
import math
img = np.zeros((600, 600, 1))
img[:]=(25)
center = [100,200]
#img = cv2.line(img,(200,200),(100,100),255)
#cv2_imshow(img)
img[:] = 255

def line(x, y, t):
  global img
  t += math.pi /2
  j, g = y
  d = 100
  h = math.cos(t)*d + g
  k = math.sin(t)*d + j
  
  #ibmg = cv2.line(img, (x), (y), 0)
  #cv2_imshow(img)
  #img = cv2.line(img, (y), (int(k),int(h)), 0)
  return int(k),int(h)
#line((0,0), (200, 200), math.radians(45))

def mfig(n):
  global img
  h = 0
  k = 0
  for x in range(n+1):
    p,q = line((0,0), (200, 200), math.radians(x*(360/n)))
    if(h!=0):
      img = cv2.line(img, (h,k), (int(p),int(q)), 0)
    h,k = p,q
    #img = cv2.line(img, )
mfig(10)
cv2.imshow("img",img)