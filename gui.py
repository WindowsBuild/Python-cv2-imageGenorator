# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 17:48:38 2020

@author: iced
"""
from tkinter import filedialog
from tkinter import *
from main import staticImage, openFile, textImage, textOverExImage
import cv2

class Window(Frame):
    
    inputFieldText = 0
    
    def getValue(self, val1):
        print(val1)
        
    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master
        self.init_window()
        
    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)
        #Entry Feild
        global e
        e = Entry(root)
        e.insert(0, "Text On The Image")
        e.pack()
        inputFieldText = e
        print(inputFieldText)
        #buttons
        b = Button(self, text='Genorate Static!', command=self.button_event_startgen)
        b.place(x=0, y=0);
        b.pack(side='bottom')
        b = Button(self, text='Select Image', command=self.button_image_text_gen)
        b.place(x=100, y=100);
        b.pack(side='bottom')
        b = Button(self, text='Get Text', command=self.getInput)
        b.place(x=150, y=150);
        b.pack(side='bottom')
    
    def getInput(self):
        s = e.get()
        textImage(s, 500, 500, cv2.FONT_HERSHEY_SIMPLEX, 200, 200, 1, 1)
        print(s)
        
    def button_event_startgen(self):
        staticImage(500,500)
        
        
    def button_image_text_gen(self):
        s = e.get()
        print('Started!')
        fileLocation =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        print(fileLocation)
        print('Loading main.py Text Modules')
        textOverExImage(fileLocation, s, 500, 500,  cv2.FONT_HERSHEY_SIMPLEX, 200, 200, 1, 1)
        
        
root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop() 