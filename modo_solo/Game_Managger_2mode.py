from Game_Managger import *


class GM_mode2(Game_Managger):
    def __init__(self, window, player_lst,order_lst):
        super().__init__(window, player_lst)
        self.order_lst = order_lst

    def create_cards(self):
        row = 0
        column = 0
        for n in range(0, len(self.card_lst)):
            if n % 6 == 0:
                row += 1
                column = 0
            self.card_lst[n].component.grid(row=row, column=column)
            column += 1

    def is_couple(self,actual_card):
        order = self.order_lst
        self.player_lst.is_playing = False
        if (actual_card.value == order[self.player_lst.plays]):
            self.player_lst.plays += 1
            self.player_lst.is_playing = True
        else:
            self.player_lst.plays = 0
            self.last_played_card = actual_card
            self.window.after(500, lambda: self.hide_cards(actual_card))

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

                id_after = self.window.after(800, lambda: self.animation_order(index + 1, id_after,last))

"""
        if index < card_lst_size:
            if id_after != None:
                self.window.after_cancel(id_after)

            self.card_lst[index].component.config(bg="yellow")
            if index != 0:
                self.card_lst[index-1].component.config(bg="white")
                self.card_lst[index-1].hide()

            id_after= self.window.after(800,lambda:self.animation_order(index+1,id_after))
        else:
            self.card_lst[card_lst_size-1].component.config(bg="white")
            self.card_lst[card_lst_size-1].hide()
            self.window.after_cancel(id_after)
"""