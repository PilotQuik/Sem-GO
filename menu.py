from tkinter import ttk
from tkinter import *
from const import *


class Menu(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        container.title("Menu")
        centerPos = container.findCenter(winHeight=MENU_HEIGHT, winWidth=MENU_WIDTH)
        container.geometry(f"{MENU_WIDTH}x{MENU_HEIGHT}+{centerPos[0]}+{centerPos[1]}")
        menuCanvas = Canvas(self, width=MENU_WIDTH, height=MENU_HEIGHT, bg='white')
        menuCanvas.pack(side=TOP, fill=BOTH, expand=NO)

        self.text = Label(menuCanvas, text="PLAY", fg="black", font=("Impact", 50), background="grey" )
        self.text.place(x=50, y=50)

        self.pack()