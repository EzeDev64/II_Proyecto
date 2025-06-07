from tkinter import *
from Card import *
from Game_Managger import *
from Player import *
import random

#Prueba de un branch
#Configurando la ventana del proyecto
window = Tk()
window.minsize(500,500)

#Creación de las clases player y el Game Managger
player = Player()
GM = Game_Managger(window,player)
lbl_time = Label(text="Time: "+str(GM.action_time))
lbl_time.pack()
#Creando las instancias de las cartas
card_lst = []
ids_lst = ["a","b","c","d","e","f","g","h","i","j","k","l","n","m","o","p","q","r"]

for n in range(0,36):
    if (n%2 == 0):
        id = ids_lst[n//2]

    card = Card(id,GM)
    card_lst.append(card)

for e in range(1,36,2):
    card_lst[e].set_couple(card_lst[e-1])
    card_lst[e-1].set_couple(card_lst[e])

#Configurando distintos aspectos del Game Mannager
GM.card_lst = card_lst
GM.shuffle()
GM.create_cards()
GM.body.pack()


window.mainloop()