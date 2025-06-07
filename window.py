from tkinter import *
from Card import *
import random

class Game_Managger:
    def __init__(self):
        self.player_plays = 0
        self.time = 0

def shuffle(lst):
    random.shuffle(lst)
    return lst

window = Tk()
window.minsize(500,500)

GM = Game_Managger()

card_lst = []
ids_lst = ["a","b","c","d","e","f","g","h","i","j","k","l","n","m","o","p","q","r"]

for n in range(0,36):
    if (n%2 == 0):
        id = ids_lst[n//2]

    card = Card(id)
    card_lst.append(card)

for e in range(1,36,2):
    card_lst[e].set_couple(card_lst[e-1])
    card_lst[e-1].set_couple(card_lst[e])

card_lst = shuffle(card_lst)

index = 0
for i in range(0,6):
    for n in range(0,6):
        card_lst[index].component.grid(row=i,column=n)
        index += 1
    
#c1.component.pack()
# c2.component.pack()
#c1.set_couple(c2)

window.mainloop()