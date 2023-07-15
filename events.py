from tkinter import *
from const import *
from main import *
from game import Game

class Event:
    def __init__(self, container):
        self.container = container
    def mouse1(self, event = NONE):
        print(int(event.x), int(event.y))
        if isinstance(self.container.frame, Menu):
            self.container.switchFrame(Game)
        elif isinstance(self.container.frame, Game):
            self.container.switchFrame(Menu)



