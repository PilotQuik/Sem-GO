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
        self.wm_attributes("-transparentcolor", TRANSPARENT)

        self.frame = Menu(self)
        self.event = Event(self)

        self.gamemode = "player"
        self.ai_level = "easy"
        self.board_size = 9

        self.board = [[0 for row in range(self.board_size)] for col in range(self.board_size)]
        print(self.board)


    def findCenter(self, winHeight, winWidth):
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()

        centerX = int(screenWidth / 2 - winWidth / 2)
        centerY = int(screenHeight / 2 - winHeight / 2)
        return (centerX, centerY)

    def switchFrame(self, newFrame, width=10, height=10):
        self.frame.pack_forget()
        self.frame = newFrame(self, width, height)

if __name__ == "__main__":
    root = Root() # creating instance of Main class
    root.bind("<Enter>", root.event.onHoverEnter)
    root.bind("<Leave>", root.event.onHoverLeave)
    root.bind("<Button-1>", root.event.mouse1) # leftclick-event
    root.bind("<Configure>", root.event.config)
    root.mainloop()