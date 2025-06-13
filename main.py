from tkinter import *
import modo_solo.window_soloMode
import window_menu, window

actual_window = None

def change_window(window_name, aw=None):
    aw.destroy()
    if window_name == "mode1":
        window.window_init()

    if window_name == "mode2":
        modo_solo.window_soloMode.window_init()

    if window_name == "main":
        window_menu.window_init()

window_menu.fnc_change = change_window
modo_solo.window_soloMode.fnc_change = change_window
window_menu.window_init()