# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 22:28:13 2020

@author: Dinesh
"""
import cv2
import imutils
img = cv2.imread('cat1.jpg')
resizeimg = imutils.resize(img, width = 500)
gaussianBlur = cv2.GaussianBlur(resizeimg,(21,21),0)
cv2.imwrite("resizedImage.jpg",resizeimg)
cv2.imshow('image',resizeimg)
grayImage = cv2.cvtColor(resizeimg,cv2.COLOR_BGR2GRAY)
thresholdImg = cv2.threshold(grayImage,100,255,cv2.THRESH_BINARY)[1]
cv2.imshow('GrayImage',grayImage)
cv2.imshow('ThresholdImage', thresholdImg)
#cv2.imshow('GaussianBlur',gaussianBlur)
cv2.waitKey(0)
cv2.destroyAllWindows()