import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import Label
from events import Event
from const import *
from menu import Menu
from game import Game


class Root(tk.Tk): # defines Main class inheriting from tk.TK
    def __init__(self):
        super().__init__() # initializing tkinter

        self.iconbitmap("assets/icon.ico")

        self.frame = Menu(self)
        self.event = Event(self)

    def findCenter(self, winHeight, winWidth):
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()

        centerX = int(screenWidth / 2 - winWidth / 2)
        centerY = int(screenHeight / 2 - winHeight / 2)
        return (centerX, centerY)

    def switchFrame(self, newFrame):
        self.frame.pack_forget()
        self.frame = newFrame(self)
"""
    def display(self, window):
        if window == "menu":
            # positions window in the center and creates the menu-canvas
            self.title("Menu")
            centerPos = self.findCenter(winHeight=MENU_HEIGHT, winWidth=MENU_WIDTH)
            self.geometry(f"{MENU_WIDTH}x{MENU_HEIGHT}+{centerPos[0]}+{centerPos[1]}")
            menuCanvas = Canvas(self, width=MENU_WIDTH, height=MENU_HEIGHT, bg='white')
            menuCanvas.pack(side=TOP, fill=BOTH, expand=NO)
            self.currentCanvas = menuCanvas


            text = Label(menuCanvas, text="PLAY", fg="black", font=("Impact", 50), background="white")
            text.place(x=50, y=50)
        if window == "game":
            # positions window in the center and creates the game-canvas
            self.title("GO")
            centerPos = self.findCenter(winHeight=GAME_HEIGHT, winWidth=GAME_WIDTH)
            self.geometry(f"{GAME_WIDTH}x{GAME_HEIGHT}+{centerPos[0]}+{centerPos[1]}")
            gameCanvas = Canvas(self, width=GAME_WIDTH, height=GAME_HEIGHT, bg='white')
            gameCanvas.pack(side=TOP, fill=BOTH, expand=NO)
            self.currentCanvas = gameCanvas

            text = Label(gameCanvas, text="go", fg="black", font=("Impact", 50), background="white")
            text.place(x=50, y=50)
        if window == "opt":
            # positions window in the center and creates the options-canvas
            self.title("Options")
            centerPos = self.findCenter(winHeight=OPT_HEIGHT, winWidth=OPT_WIDTH)
            self.geometry(f"{OPT_WIDTH}x{OPT_HEIGHT}+{centerPos[0]}+{centerPos[1]}")
            optCanvas = Canvas(self, width=OPT_WIDTH, height=OPT_HEIGHT, bg='white')
            optCanvas.pack(side=TOP, fill=BOTH, expand=NO)
            self.currentCanvas = optCanvas

            text = Label(optCanvas, text="options", fg="black", font=("Impact", 50), background="white")
            text.place(x=50, y=50)     
"""
if __name__ == "__main__":
    root = Root() # creating instance of Main class
    root.bind("<Button-1>", root.event.mouse1) # leftclick-event
    root.mainloop()