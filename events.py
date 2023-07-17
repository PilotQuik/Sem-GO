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
        print(int(event.x), int(event.y), event.widget, str(event.widget).split(".")[-1])
        if isinstance(self.container.frame, Menu):
            if str(event.widget).split(".")[-1] == "play-button":
                self.container.switchFrame(Game)
            if str(event.widget).split(".")[-1] == "opt-button":
                self.container.switchFrame(Opt)
            if str(event.widget).split(".")[-1] == "quit-button":
                self.container.destroy()
        elif isinstance(self.container.frame, Game):
            if ".!canvas.!label" in str(event.widget):
                self.container.switchFrame(Opt)
        elif isinstance(self.container.frame, Opt):
            if ".!canvas.!label" in str(event.widget):
                self.container.switchFrame(Menu)



