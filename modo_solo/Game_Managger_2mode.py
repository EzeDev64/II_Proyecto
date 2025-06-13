from Game_Managger import *
from Card import *


class GM_mode2(Game_Managger):
    def __init__(self, window, lbl_timer, player_lst,order_lst):
        super().__init__(window, player_lst)
        self.action_time = 12
        self.lbl_timer = lbl_timer
        self.time_stop = False
        self.order_lst = order_lst
        self.after_stack = []
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
        self.time_stop = True
        self.action_time += 3
        self.lbl_timer.config(text="Time: " + str(self.action_time))

        if self.order_lst == self.lst_full:
            print("GANASTE")
            return

        for e in self.card_lst:
            e.component.grid_forget()
            del e
        self.card_lst = []
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
        self.player_lst.is_playing = False
        card_lst_size = len(self.card_lst)
        if index >= card_lst_size:
            last.component.config(bg="white")
            last.hide()
            self.window.after_cancel(id_after)
            self.time_stop = False
            self.timer_start()
            self.player_lst.is_playing = True
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

    def timer_start(self):
        if self.after_stack != []:
            self.window.after_cancel(self.after_stack[0])
            self.after_stack.pop(0)
        if  self.action_time <= 0:
            self.window.after_cancel(self.after_stack[0])
            self.after_stack.pop(0)
            print("Perdiste :(")
            self.player_lst.is_playing= False
            return

        if not self.time_stop:
            self.action_time -= 1
            self.lbl_timer.config(text="Time: " + str(self.action_time))
            self.after_stack.append(self.window.after(1000, self.timer_start))

    def cancel_afters(self):
        while self.after_stack != []:
            self.window.after_cancel(self.after_stack[0])
            self.after_stack.pop(0)

