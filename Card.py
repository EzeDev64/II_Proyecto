from tkinter import *

class Card:
    def __init__(self,value):
        self.couple = None
        self.value = value
        self.component = Button(text=self.value,width=10,command=self.show)
        
        self.hide()

    def set_couple(self,couple):
        self.couple = couple

    def hide(self):
        self.component.config(bg="red",text="")
    
    def show(self):
        print(self.couple,self.couple.value)
        self.component.config(bg="white",text= self.value)