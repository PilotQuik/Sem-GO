from tkinter import ttk
from tkinter import *
from const import *


class Game(ttk.Frame):
    def __init__(self, container, width=GAME_WIDTH, height=GAME_HEIGHT):
        super().__init__(container)

        self.container = container
        self.width = width
        self.height = height

        self.container.title("Menu")
        self.container.resizable(True, True)
        self.container.minsize(GAME_WIDTH//2, GAME_HEIGHT//2)

        centerPos = self.container.findCenter(winHeight=self.height, winWidth=self.width)
        self.container.geometry(f"{self.width}x{self.height}+{centerPos[0]}+{centerPos[1]}")

        self.displayCanvas()

    def displayCanvas(self):
        self.canvas = Canvas(self, width=10000, height=10000, bg='white')
        self.canvas.pack(side=TOP, fill=BOTH, expand=NO)

        text = Label(self.canvas, text="Back", fg="black", font=("Impact", 50), background="grey")
        text.place(x=50, y=50)

        self.pack()

    def displayBoard(self):
        self.canvas.create_rectangle(50, 50, self.container.winfo_width() - 50, self.container.winfo_height() - 50)
        print("-----------Board")