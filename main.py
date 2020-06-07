# -*- coding: utf-8 -*-
"""
Made By Windows <3
"""
import cv2
import numpy as np


fontColor = (255,255,255)
def textImage(text, width, height, font, textX, textY,fontScale, lineType):
    img = np.zeros((width,height,3), np.uint8)
    
    cv2.putText(img,'Hello World!', 
        (textX, textY), 
        font, 
        fontScale,
        fontColor,
        lineType)
    cv2.imshow("img",img)
    cv2.imwrite("out.jpg", img)
    cv2.waitKey(0)
    

def staticImage(width, height):
    print('Started Genoration')
    img = np.random.randint(222, size=(width, height,3))
    gen = np.array(img ,dtype=np.uint8)
    cv2.imshow('i',gen)
    cv2.waitKey(0)
    cv2.destroyWindow('i')
    print('finished')
    
    

def commandLineInterface():
    print('Create an Image! enter in the args below:')
    text = input('Enter Image Text: ')
    imageHeight = int(input('Enter Image Height: '))
    imageWidth = int(input('Enter Image Width: '))
    font = input('Enter Font (enter default for default): ')
    textX = int(input('Enter textX Position(enter center for text in the center): '))
    textY = int(input('Enter textY Position(enter center for text in the center): '))
    fontScale = int(input('Font Size(int): '))
    lineType = int(input('Line type(int): '))
    textImage(text, imageHeight, imageWidth, cv2.FONT_HERSHEY_SIMPLEX, textX, textY, fontScale, fontScale)
    save = input('Would you like to save?')
    
    
    
commandLineInterface()
    
    

     
