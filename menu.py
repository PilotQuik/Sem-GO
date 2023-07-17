from tkinter import ttk
from tkinter import *
from const import *
from button import Button_

class Menu(ttk.Frame):
    def __init__(self, container, width=MENU_WIDTH, height=MENU_HEIGHT):
        super().__init__(container)

        self.width = width
        self.height = height

        container.title("Menu")
        container.minsize(MENU_WIDTH, MENU_HEIGHT)
        centerPos = container.findCenter(winHeight=self.height, winWidth=self.width)
        container.geometry(f"{self.width}x{self.height}+{centerPos[0]}+{centerPos[1]}")
        self.menuCanvas = Canvas(self, width=self.width, height=self.height, bg=BACKGROUND)
        self.menuCanvas.pack(side=TOP, fill=BOTH, expand=NO)

        self.play_button = Button_(40, 20, self.menuCanvas, name="play-button", text="PLAY", font=(FONT, 95, "bold"))
        self.opt_button = Button_(45, 150, self.menuCanvas, name="opt-button", text="OPTIONS", font=(FONT, 40, "bold"))
        self.opt_button = Button_(45, 210, self.menuCanvas, name="rules-button", text="RULES", font=(FONT, 40, "bold"))
        self.opt_button = Button_(45, 270, self.menuCanvas, name="load-button", text="LOAD", font=(FONT, 40, "bold"))
        self.quit_button = Button_(45, 330, self.menuCanvas, name="quit-button", text="QUIT", font=(FONT, 40, "bold"))

        self.menuCanvas.create_rectangle(430, 50, self.width - 50, self.height - 50, fill=TRANSPARENT)

        self.pack()
