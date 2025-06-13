from tkinter import *


fnc_change = None

def window_init():
    window = Tk()
    window.minsize(500, 500)

    lbl_title = Label(text="Memory game")
    lbl_title.pack()

    frame_modes = Frame()
    btn_mode1 = Button(frame_modes, text="Modo clásico",command=lambda: fnc_change("mode1",window))
    btn_mode2 = Button(frame_modes, text="Modo solo",command=lambda: fnc_change("mode2",window))
    btn_prices = Button(frame_modes, text="Prices")

    btn_mode1.pack()
    btn_mode2.pack()
    btn_prices.pack()
    frame_modes.pack()

    frame_footer = Frame()
    btn_log = Button(frame_footer, text="LogOut")
    btn_log.pack(side="left")
    frame_footer.pack(fill="x", side="bottom")
    window.mainloop()

def change_functions(fnc):
    btn_mode1.config(command=lambda:fnc("mode1",window))
    btn_mode2.config(command=lambda:fnc("mode2",window))
    #btn_prices.config(command=lambda:fnc(""))


