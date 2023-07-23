from tkinter import ttk
from tkinter import *
from const import *
from main import *


class Game(ttk.Frame):
    def __init__(self, container, width=GAME_WIDTH, height=GAME_HEIGHT):
        super().__init__(container)

        self.container = container
        self.width = width
        self.height = height
        self.pad = 50

        self.container.title("Menu")
        self.container.resizable(True, True)
        self.container.minsize(GAME_WIDTH//2, GAME_HEIGHT//2)

        centerPos = self.container.findCenter(winHeight=self.height, winWidth=self.width)
        self.container.geometry(f"{self.width}x{self.height}+{centerPos[0]}+{centerPos[1]}")

        self.displayCanvas()

    def displayCanvas(self):
        self.canvas = Canvas(self, width=10000, height=10000, bg='white')
        self.canvas.pack(side=TOP, fill=BOTH, expand=NO)

        text = Label(self.canvas, text="Back", fg="black", font=("Impact", 20), background="grey")
        text.place(x=0, y=0)

        self.pack()

    def displayBoard(self):
        len = int(min(self.container.winfo_width(), self.container.winfo_height()))
        self.canvas.create_rectangle(self.pad, self.pad, len - self.pad, len - self.pad, fill="#c9833c",
                                     outline="#c9833c")
        length = int(len - (2 * self.pad))
        boardPad = length / (self.container.board_size + 1)
        tile = length / self.container.board_size
        i = 0
        # draw board
        for row in range(self.container.board_size):
            self.canvas.create_line(self.pad + boardPad, self.pad + boardPad + i * boardPad, len - boardPad - self.pad,
                                    self.pad + boardPad + i * boardPad)
            for col in range(self.container.board_size):
                self.canvas.create_line(self.pad + boardPad + i * boardPad, self.pad + boardPad, self.pad + boardPad + i * boardPad,len - self.pad - boardPad)
            i += 1

    def drawStone(self):
        pass