from tkinter import ttk
from tkinter import *
from const import *


class Opt(ttk.Frame):
    def __init__(self, container, width=OPT_WIDTH, height=OPT_HEIGHT):
        super().__init__(container)

        self.container = container
        self.width = width
        self.height = height

        self.container.title("Options")
        self.container.resizable(False, False)
        self.container.minsize(OPT_WIDTH, OPT_HEIGHT)

        centerPos = self.container.findCenter(winHeight=self.height, winWidth=self.width)
        self.container.geometry(f"{self.width}x{self.height}+{centerPos[0]}+{centerPos[1]}")

        self.displayCanvas()

    def displayCanvas(self):
        canvas = Canvas(self, width=self.width, height=self.height, bg='white')
        canvas.pack(side=TOP, fill=BOTH, expand=NO)

        self.text = Label(canvas, text="Back", fg="black", font=("Impact", 50), background="grey" )
        self.text.place(x=50, y=50)

        self.pack()