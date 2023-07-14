import tkinter as tk
from tkinter import Label
from tkinter import ttk
from const import *

class MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        options = {"padx": 10, "pady": 10}

        text = Label(root, text="PLAY", fg="black", font=("Impact", 50))
        text.place(x=50, y=50)

class App(tk.Tk): # defines Main class inheriting from tk.TK
    def __init__(self):
        super().__init__() # initializing tkinter

        self.title("Main")
        self.geometry(str(MENU_WIDTH) + "x" + str(MENU_HEIGHT))
        self.wm_iconphoto(False, tk.PhotoImage(file="assets/icon.png"))

if __name__ == "__main__":
    root = App() # creating instance of Main class
    frame = MainFrame(root)
    root.mainloop()



#root = Tk()

# menu window:
#if CURRENT_WINDOW == "menu":
#    root.title("MENU")
#    root.wm_iconphoto(False, tkinter.PhotoImage(file="assets/icon.png"))
#    menuCanvas = Canvas(root, width=MENU_WIDTH, height=MENU_HEIGHT, bg='yellow')
#    menuCanvas.pack(side=TOP, fill=BOTH, expand=YES)

# game window
#if CURRENT_WINDOW == "game":
#    root.title("GO")
#    root.wm_iconphoto(False, tkinter.PhotoImage(file="assets/icon.png"))
#    gameCanvas = Canvas(root, width=MENU_WIDTH, height=MENU_HEIGHT, bg='brown')
#    gameCanvas.pack(side=TOP, fill=BOTH, expand=YES)

# options window
#if CURRENT_WINDOW == "opt":
#    root.title("OPTIONS")
#    root.wm_iconphoto(False, tkinter.PhotoImage(file="assets/icon.png"))
#    optCanvas = Canvas(root, width=MENU_WIDTH, height=MENU_HEIGHT, bg='white')
#    optCanvas.pack(side=TOP, fill=BOTH, expand=YES)

###>----------mainloop----------<###

###>----------mainloop----------<###
#root.mainloop()