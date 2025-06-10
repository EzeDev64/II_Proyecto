from Game_Managger import *
from Card import *


class GM_mode2(Game_Managger):
    def __init__(self, window, player_lst,order_lst):
        super().__init__(window, player_lst)
        self.order_lst = order_lst
        self.lst_full = None

    def set_full_lst(self,lst_full):
        self.lst_full = lst_full

    def create_cards(self):
        row = 0
        column = 0
        for n in range(0, len(self.card_lst)):
            if n % 6 == 0:
                row += 1
                column = 0
            self.card_lst[n].component.grid(row=row, column=column)
            column += 1

    def next_round(self):
        for e in self.card_lst:
            e.component.grid_forget()
            del e
        self.card_lst = []
        element = 1
        self.order_lst.append(self.lst_full[len(self.order_lst)])

        for i in self.order_lst:
            card = Card(i, self, False)
            self.card_lst.append(card)

        self.shuffle()
        self.create_cards()
        self.animation_order(0, None, 0)
        self.player_lst.is_playing = True
        self.player_lst.plays = 0

    def is_couple(self,actual_card):
        order = self.order_lst
        self.player_lst.is_playing = False

        if (actual_card.value == order[-1] and self.player_lst.plays == len(order)-1):
            self.next_round()
            return
        if (actual_card.value == order[self.player_lst.plays]):
            self.player_lst.plays += 1
            self.player_lst.is_playing = True
        else:
            self.player_lst.plays = 0
            for e in self.card_lst:
                e.hide()
                e.active = False
                self.player_lst.is_playing = True
            self.last_played_card = actual_card
            #self.window.after(500, lambda: self.hide_cards(actual_card))

    def animation_order(self,index,id_after,last):
        card_lst_size = len(self.card_lst)
        if index >= card_lst_size:
            last.component.config(bg="white")
            last.hide()
            self.window.after_cancel(id_after)
            return

        for i in self.card_lst:
            if i.value == self.order_lst[index]:
                if id_after != None:
                    self.window.after_cancel(id_after)

                i.component.config(bg="yellow")
                if index != 0:
                    last.component.config(bg="white")
                    last.hide()
                last = i

                id_after = self.window.after(500, lambda: self.animation_order(index + 1, id_after,last))
