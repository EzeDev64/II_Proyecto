from tkinter import *
from Player import *
from modo_solo.Game_Managger_2mode import *
from Game_Managger import *
from Card import *

fnc_change = None

def window_init():
    window = Tk()
    window.minsize(500,500)
    lbl_time = Label(text="Time: ")

    #Creación del jugador,cartas y el mannager
    player = Player()
    card_lst = []
    ids_lst = ["1","2","3"]
    order_lst = ids_lst.copy()

    GM = GM_mode2(window,lbl_time,player,order_lst)
    for n in ids_lst:
        card = Card(n,GM,False)
        card_lst.append(card)

    ids_lst= ["1","2","3","4","5","6","7","8","9","10","11","12"]
    GM.set_full_lst(ids_lst)

    #Configurando distintos aspectos del Game Mannager
    lbl_time.configure(text="Time: "+ str(GM.action_time))
    lbl_time.pack()
    GM.card_lst = card_lst
    GM.shuffle()
    GM.create_cards()
    GM.body.pack()
    GM.animation_order(0,None,0)

    frame = Frame()
    btn_return = Button(frame,text="Return",command = lambda: close_window(GM,window) )
    btn_return.pack(side="right",padx=5,pady=5)
    frame.pack(side="bottom",fill="x")

    window.mainloop()


def close_window(GM,window):
    GM.cancel_afters()
    fnc_change("main", window)