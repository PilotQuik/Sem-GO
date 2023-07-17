from tkinter import ttk
from tkinter import *
from const import *


class Game(ttk.Frame):
    def __init__(self, container, width=GAME_WIDTH, height=GAME_HEIGHT):
        super().__init__(container)

        self.width = width
        self.height = height

        container.title("Menu")
        centerPos = container.findCenter(winHeight=self.height, winWidth=self.width)
        container.geometry(f"{self.width}x{self.height}+{centerPos[0]}+{centerPos[1]}")
        gameCanvas = Canvas(self, width=self.width, height=self.height, bg='white')
        gameCanvas.pack(side=TOP, fill=BOTH, expand=NO)

        text = Label(gameCanvas, text="Back", fg="black", font=("Impact", 50), background="grey")
        text.place(x=50, y=50)

        self.pack()