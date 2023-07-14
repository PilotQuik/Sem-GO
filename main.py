import tkinter
from const import *
from tkinter import *

root = Tk()
# menu window:
if CURRENT_WINDOW == "menu":
    root.title("MENU")
    root.wm_iconphoto(False, tkinter.PhotoImage(file="assets/icon.png"))
    menuCanvas = Canvas(root, width=MENU_WIDTH, height=MENU_HEIGHT, bg='yellow')
    menuCanvas.pack(side=TOP, fill=BOTH, expand=YES)

# game window
if CURRENT_WINDOW == "game":
    root.title("GO")
    root.wm_iconphoto(False, tkinter.PhotoImage(file="assets/icon.png"))
    gameCanvas = Canvas(root, width=MENU_WIDTH, height=MENU_HEIGHT, bg='brown')
    gameCanvas.pack(side=TOP, fill=BOTH, expand=YES)

# options window
if CURRENT_WINDOW == "opt":
    root.title("OPTIONS")
    root.wm_iconphoto(False, tkinter.PhotoImage(file="assets/icon.png"))
    optCanvas = Canvas(root, width=MENU_WIDTH, height=MENU_HEIGHT, bg='white')
    optCanvas.pack(side=TOP, fill=BOTH, expand=YES)

###>----------mainloop----------<###

###>----------mainloop----------<###
root.mainloop()