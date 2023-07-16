from tkinter import ttk
from tkinter import *
from const import *


class Game(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        container.title("Menu")
        centerPos = container.findCenter(winHeight=GAME_HEIGHT, winWidth=GAME_WIDTH)
        container.geometry(f"{GAME_WIDTH}x{GAME_HEIGHT}+{centerPos[0]}+{centerPos[1]}")
        gameCanvas = Canvas(self, width=GAME_WIDTH, height=GAME_HEIGHT, bg='white')
        gameCanvas.pack(side=TOP, fill=BOTH, expand=NO)

        text = Label(gameCanvas, text="Game", fg="black", font=("Impact", 50), background="grey")
        text.place(x=50, y=50)

        self.pack()