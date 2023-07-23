from tkinter import ttk
from tkinter import *
from const import *
from main import *
from custom import Button_


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

        centerPos = self.container.findCenter(winHeight=self.width, winWidth=self.height)
        self.container.geometry(f"{self.width}x{self.height}+{centerPos[0]}+{centerPos[1]}")

        self.displayCanvas()

    def displayCanvas(self):
        self.canvas = Canvas(self, width=10000, height=10000, bg='white')
        self.canvas.pack(side=TOP, fill=BOTH, expand=NO)

        Button_(3, 5, self.canvas, name="back-button", text="<<",
                font=(FONT, 25, "bold"))
        self.pack()

    def displayBoard(self):
        len = int(min(self.container.winfo_width(), self.container.winfo_height()))
        self.canvas.create_rectangle(self.pad, self.pad, len - self.pad, len - self.pad, fill="#c9833c",
                                     outline="#c9833c")
        length = int(len - (2 * self.pad))
        boardPad = length / (self.container.board.size + 1)
        # draw board
        for row in range(self.container.board.size):
            self.canvas.create_line(self.pad + boardPad, self.pad + boardPad + row * boardPad,
                                    len - boardPad - self.pad, self.pad + boardPad + row * boardPad)
            for col in range(self.container.board.size):
                self.canvas.create_line(self.pad + boardPad + col * boardPad, self.pad + boardPad,
                                        self.pad + boardPad + col * boardPad,len - self.pad - boardPad)

                if self.container.board.size == 19 and row in (3, 9, 15) and col in (3, 9, 15):
                    self.canvas.create_oval(self.pad + boardPad + col * boardPad - 3,
                                            self.pad + boardPad + row * boardPad - 3,
                                            self.pad + boardPad + col * boardPad + 3,
                                            self.pad + boardPad + row * boardPad + 3, fill="black")
                elif self.container.board.size == 13 and (row, col) in ((3, 3), (9, 3), (3, 9), (9, 9), (6, 6)):
                    self.canvas.create_oval(self.pad + boardPad + col * boardPad - 3,
                                            self.pad + boardPad + row * boardPad - 3,
                                            self.pad + boardPad + col * boardPad + 3,
                                            self.pad + boardPad + row * boardPad + 3, fill="black")
                elif self.container.board.size == 9 and (row, col) in ((2, 2), (6, 2), (2, 6), (6, 6), (4, 4)):
                    self.canvas.create_oval(self.pad + boardPad + col * boardPad - 3,
                                            self.pad + boardPad + row * boardPad - 3,
                                            self.pad + boardPad + col * boardPad + 3,
                                            self.pad + boardPad + row * boardPad + 3, fill="black")

    def drawStone(self):
        pass