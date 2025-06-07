from tkinter import *

class Card:
    def __init__(self,value,managger):
        self.couple = None
        self.value = value
        self.component = Button(managger.body,text=self.value,width=10,command=self.show)
        self.managger = managger
        self.active = False
        self.hide()

    def set_couple(self,couple):
        self.couple = couple

    def hide(self):
        self.component.config(bg="red",text="")
    
    def show(self):
        if self.active == True:
            return
        if self.managger.player_lst.is_playing == False:
            return

        self.active = True
        self.component.config(bg="white",text= self.value)
        self.managger.is_couple(self)

