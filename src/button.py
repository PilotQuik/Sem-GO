from tkinter import *
from const import *

class Button_(Label):
    def __init__(self, x, y, container, name="!label", text="", fg=BUTTON_COL, font=("Impact", 10), background=BACKGROUND, cursor="hand2"):
        super().__init__(container)

        self.container = container
        self.x = x
        self.y = y
        self.name = name
        self.text = text
        self.fg = fg
        self.font = font
        self.background = background
        self.cursor = cursor

        self.button = Label(self.container, name=self.name, text=self.text, fg=self.fg, font=self.font,
                                 background=self.background, cursor=self.cursor)
        self.button.place(x=self.x, y=self.y)