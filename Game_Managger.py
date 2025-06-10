from tkinter import *
import time, random

class Game_Managger:
    def __init__(self,window,player_lst):
        self.card_lst = []
        self.window = window
        self.body = Frame(window,bg="blue",width=400,height=400)
        self.action_time = 0
        self.player_lst = player_lst
        self.last_played_card = None
        #self.grid_size = grid_size

    def shuffle(self):
        random.shuffle(self.card_lst)

    def is_couple(self,actual_card):
        #Confirma si solo existe una una carta escogida o si se escoge la misma
        #En caso contrario de ambos, comprueba si son iguales o diferentes
        if self.last_played_card == None:
            self.last_played_card = actual_card
        elif actual_card == self.last_played_card:
            return
        elif self.last_played_card.value == actual_card.value:
            #En caso de ser iguales, las coloca como pares y se voltean para siempre
            self.last_played_card = None
        else:
            #En caso de ser diferentes, llama la función *hide_cards para ocultarlas
            #Hace que el estado *is_playing del player sea falso para eviar bugs al rápidamente seleccionar una tercera carta
            self.player_lst.is_playing = False
            self.window.after(500,lambda: self.hide_cards(actual_card))

    def hide_cards(self,card):
        #Oculta las cartas y de nuevo hace que el jugador pueda seleccionar cartas
        self.last_played_card.hide()
        card.hide()
        card.active = False
        self.last_played_card.active = False
        self.last_played_card = None
        self.player_lst.is_playing = True

    def sum_player_points(self,actual_player):
        actual_player.points += 0

    def put_sec(self):
        self.action_time += 0

    def create_cards(self):
        index = 0
        for i in range(0,6):
            for n in range(0,6):
                self.card_lst[index].component.grid(row=i, column=n)
                index += 1