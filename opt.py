from tkinter import ttk
from tkinter import *
from const import *


class Opt(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        container.title("Options")
        centerPos = container.findCenter(winHeight=OPT_HEIGHT, winWidth=OPT_WIDTH)
        container.geometry(f"{OPT_WIDTH}x{OPT_HEIGHT}+{centerPos[0]}+{centerPos[1]}")
        menuCanvas = Canvas(self, width=OPT_WIDTH, height=OPT_HEIGHT, bg='white')
        menuCanvas.pack(side=TOP, fill=BOTH, expand=NO)

        self.text = Label(menuCanvas, text="Options", fg="black", font=("Impact", 50), background="grey" )
        self.text.place(x=50, y=50)

        self.pack()