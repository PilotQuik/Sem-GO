from tkinter import *

from const import *
from stone import Stone
from custom import Button_

class Menu(Label):
    def __init__(self, container, width=MENU_WIDTH, height=MENU_HEIGHT):
        super().__init__(container)

        self.container = container
        self.width = width
        self.height = height

        self.container.title("Menu")
        self.container.resizable(False, False)
        self.container.minsize(MENU_WIDTH, MENU_HEIGHT)

        centerPos = self.container.findCenter(winHeight=self.height, winWidth=self.width)
        self.container.geometry(f"{self.width}x{self.height}+{centerPos[0]}+{centerPos[1]}")

        self.displayCanvas()

    def displayCanvas(self):
        self.canvas = Canvas(self, width=self.width, height=self.height, bg=BACKGROUND)
        self.canvas.pack(side=TOP, fill=BOTH, expand=NO)

        self.play_button = Button_(40, 20, self.canvas, name="play-button", text="PLAY", font=(FONT, 95, "bold"))
        self.opt_button = Button_(45, 150, self.canvas, name="opt-button", text="OPTIONS", font=(FONT, 40, "bold"))
        self.opt_button = Button_(45, 210, self.canvas, name="rules-button", text="RULES", font=(FONT, 40, "bold"))
        self.opt_button = Button_(45, 270, self.canvas, name="load-button", text="LOAD", font=(FONT, 40, "bold"))
        self.quit_button = Button_(45, 330, self.canvas, name="quit-button", text="QUIT", font=(FONT, 40, "bold"))

        #self.canvas.create_rectangle(430, 50, self.width - 50, self.height - 50, fill="white")
        self.displayBoard()

        self.pack()

    def displayBoard(self):
        pad = 50
        padLeft = self.width - self.height + pad
        self.canvas.create_rectangle(padLeft, 50, self.width - 50, self.height - 50, fill="#c9833c",
                                     outline="black")
        length = int(self.height - (2 * pad))
        self.boardPad = length / (self.container.board.size + 1)
        # draw board
        for row in range(self.container.board.size):
            self.canvas.create_line(padLeft + self.boardPad, pad + self.boardPad + row * self.boardPad,
                                    self.width - self.boardPad - pad, pad + self.boardPad + row * self.boardPad)
            for col in range(self.container.board.size):
                self.canvas.create_line(padLeft + self.boardPad + col * self.boardPad, pad + self.boardPad,
                                        padLeft + self.boardPad + col * self.boardPad, self.height - pad - self.boardPad)

                if self.container.board.size == 19 and row in (3, 9, 15) and col in (3, 9, 15):
                    self.canvas.create_oval(padLeft + self.boardPad + col * self.boardPad - 3,
                                            pad + self.boardPad + row * self.boardPad - 3,
                                            padLeft + self.boardPad + col * self.boardPad + 3,
                                            pad + self.boardPad + row * self.boardPad + 3, fill="black")
                elif self.container.board.size == 13 and (row, col) in ((3, 3), (9, 3), (3, 9), (9, 9), (6, 6)):
                    self.canvas.create_oval(padLeft + self.boardPad + col * self.boardPad - 3,
                                            pad + self.boardPad + row * self.boardPad - 3,
                                            padLeft + self.boardPad + col * self.boardPad + 3,
                                            pad + self.boardPad + row * self.boardPad + 3, fill="black")
                elif self.container.board.size == 9 and (row, col) in ((2, 2), (6, 2), (2, 6), (6, 6), (4, 4)):
                    self.canvas.create_oval(padLeft + self.boardPad + col * self.boardPad - 3,
                                            pad + self.boardPad + row * self.boardPad - 3,
                                            padLeft + self.boardPad + col * self.boardPad + 3,
                                            pad + self.boardPad + row * self.boardPad + 3, fill="black")
        for col in range(self.container.board.size):
            for row in range(self.container.board.size):
                if isinstance(self.container.board.positions[col][row], Stone):
                    self.container.board.positions[col][row].boardPad = self.boardPad
                    self.container.board.positions[col][row].draw(self.canvas, "Menu")