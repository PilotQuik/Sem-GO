import re
from tkinter import *
from const import *
from main import *
from game import Game
from opt import Opt


class Event:
    def __init__(self, container):
        self.container = container
    def mouse1(self, event = NONE):
        #print(int(event.x), int(event.y), event.widget)
        if isinstance(self.container.frame, Menu):
            if str(event.widget).split(".")[-1] == "play-button":
                self.container.switchFrame(Game, width=GAME_WIDTH, height=GAME_HEIGHT)
            if str(event.widget).split(".")[-1] == "opt-button":
                self.container.switchFrame(Opt, width=OPT_WIDTH, height=OPT_HEIGHT)
            if str(event.widget).split(".")[-1] == "quit-button":
                self.container.destroy()
        elif isinstance(self.container.frame, Game):
            if ".!canvas" in str(event.widget):
                self.container.switchFrame(Menu, width=MENU_WIDTH, height=MENU_HEIGHT)
        elif isinstance(self.container.frame, Opt):
            if ".!canvas.!label" in str(event.widget):
                self.container.switchFrame(Menu, width=MENU_WIDTH, height=MENU_HEIGHT)

    def onHoverEnter(self, event=None):
        if "-button" in str(event.widget).split(".")[-1]:
            event.widget.config(fg=BUTTON_COL_CLICKED)

    def onHoverLeave(self, event=None):
        if "-button" in str(event.widget).split(".")[-1]:
            event.widget.config(fg=BUTTON_COL)

    def config(self, event=None):
        #print(event.widget, event.width, event.height)
        #print(self.container.winfo_width(), self.container.winfo_height())
        if isinstance(event.widget, Canvas) and isinstance(self.container.frame, Game):
            if int(self.container.winfo_width()) == int(event.width) and int(self.container.winfo_height()) == int(event.height):
                self.container.frame.canvas.delete("all")
                self.container.frame.displayBoard()


