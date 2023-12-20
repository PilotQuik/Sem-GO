import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import Label

from events import Event
from const import *
from menu import Menu
from game import Game
from board import Board


class Root(tk.Tk):
    def __init__(self):
        super().__init__()

        self.iconbitmap("assets/icon.ico")

        self.gamemode = "player"
        self.ai_level = "easy"
        self.theme = "classic"
        self.board = Board(self, 9)

        self.background = BACKGROUND
        self.button_col = BUTTON_COL
        self.button_col_clicked = BUTTON_COL_CLICKED
        self.button_col_selected = BUTTON_COL_SELECTED
        self.board_col = BOARD_COL
        self.board_line = BOARD_LINE
        self.hover_b = HOVER_B
        self.hover_w = HOVER_W

        self.frame = Menu(self)
        self.event = Event(self)

        self.aiFirst = False
        self.easteregg = False

    def refresh(self):
        if isinstance(self.frame, Game):
            self.frame.canvas.delete("all")
            self.frame.displayBoard()
            self.board.displayStones()

    def findCenter(self, winHeight, winWidth):
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()

        centerX = int(screenWidth / 2 - winWidth / 2)
        centerY = int(screenHeight / 2 - winHeight / 2)
        return (centerX, centerY)

    def switchFrame(self, newFrame, width=10, height=10):
        self.frame.pack_forget()
        self.frame = newFrame(self, width, height)

        if self.aiFirst and newFrame == Game:
            self.frame.makeMoveAI()
            self.aiFirst = False

if __name__ == "__main__":
    root = Root()
    root.bind("<Motion>", root.event.motion)
    root.bind("<Enter>", root.event.onHoverEnter)
    root.bind("<Leave>", root.event.onHoverLeave)
    root.bind("<Button-3>", root.event.mouse3)  # rightclick-event
    root.bind("<Button-1>", root.event.mouse1) # leftclick-event
    root.bind("<Configure>", root.event.config)
    root.mainloop()