from tkinter import *
from const import *
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

        self.canvas.create_rectangle(430, 50, self.width - 50, self.height - 50, fill="white")

        self.pack()
