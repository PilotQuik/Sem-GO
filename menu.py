from tkinter import ttk
from tkinter import *
from const import *
from button import Button_


class Menu(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        container.title("Menu")
        centerPos = container.findCenter(winHeight=MENU_HEIGHT, winWidth=MENU_WIDTH)
        container.geometry(f"{MENU_WIDTH}x{MENU_HEIGHT}+{centerPos[0]}+{centerPos[1]}")
        menuCanvas = Canvas(self, width=MENU_WIDTH, height=MENU_HEIGHT, bg='white')
        menuCanvas.pack(side=TOP, fill=BOTH, expand=NO)

        self.play_button = Button_(50, 50, menuCanvas, name="play-button", text="PLAY", fg="black", font=("Impact", 50),
                            background="white", cursor="hand2")
        self.opt_button = Button_(50, 150, menuCanvas, name="opt-button", text="OPTIONS", fg="black", font=("Impact", 30),
                                   background="white", cursor="hand2")
        self.quit_button = Button_(50, 200, menuCanvas, name="quit-button", text="QUIT", fg="black", font=("Impact", 30),
                                   background="white", cursor="hand2")
        self.pack()