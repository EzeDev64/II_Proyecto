from tkinter import *
from Player import *
from Game_Managger_2mode import *
from Game_Managger import *
from Card import *

window = Tk()
window.minsize(500,500)

#Creación del jugador,cartas y el mannager
player = Player()
card_lst = []
ids_lst = ["1","2","3"]
order_lst = ids_lst.copy()

GM = GM_mode2(window,player,order_lst)
for n in ids_lst:
    card = Card(n,GM,False)
    card_lst.append(card)

ids_lst= ["1","2","3","4","5","6","7","8","9","10","11","12"]
GM.set_full_lst(ids_lst)

#Configurando distintos aspectos del Game Mannager
GM.card_lst = card_lst
GM.shuffle()
GM.create_cards()
GM.body.pack()
GM.animation_order(0,None,0)

window.mainloop()

