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
            elif str(event.widget).split(".")[-1] == "opt-button":
                self.container.switchFrame(Opt, width=OPT_WIDTH, height=OPT_HEIGHT)
            elif str(event.widget).split(".")[-1] == "quit-button":
                self.container.destroy()
        elif isinstance(self.container.frame, Game):
            if ".!canvas" in str(event.widget):
                self.container.switchFrame(Menu, width=MENU_WIDTH, height=MENU_HEIGHT)
        elif isinstance(self.container.frame, Opt):
            if str(event.widget).split(".")[-1] == "back-button":
                self.container.switchFrame(Menu, width=MENU_WIDTH, height=MENU_HEIGHT)
            elif str(event.widget).split(".")[-1] == "play-button":
                self.container.switchFrame(Game, width=GAME_WIDTH, height=GAME_HEIGHT)
            # gamemode
            elif str(event.widget).split(".")[-1] == "vs-player-button":
                self.container.gamemode = "player"
                self.container.frame.displayCanvas()
            elif str(event.widget).split(".")[-1] == "vs-ai-button":
                self.container.gamemode = "ai"
                self.container.frame.displayCanvas()
            # ai level
            elif str(event.widget).split(".")[-1] == "easy-ai-button":
                self.container.ai_level = "easy"
                self.container.frame.displayCanvas()
            elif str(event.widget).split(".")[-1] == "medium-ai-button":
                self.container.ai_level = "medium"
                self.container.frame.displayCanvas()
            elif str(event.widget).split(".")[-1] == "hard-ai-button":
                self.container.ai_level = "hard"
                self.container.frame.displayCanvas()
            # board size
            elif str(event.widget).split(".")[-1] == "9x9-button":
                self.container.board.size = 9
                self.container.frame.displayCanvas()
            elif str(event.widget).split(".")[-1] == "13x13-button":
                self.container.board.size = 13
                self.container.frame.displayCanvas()
            elif str(event.widget).split(".")[-1] == "19x19-button":
                self.container.board.size = 19
                self.container.frame.displayCanvas()
            # theme
            elif str(event.widget).split(".")[-1] == "classic-button":
                self.container.theme = "classic"
                self.container.frame.displayCanvas()
            elif str(event.widget).split(".")[-1] == "minimal-button":
                self.container.theme = "minimal"
                self.container.frame.displayCanvas()
            elif str(event.widget).split(".")[-1] == "error-button":
                self.container.theme = "error"
                self.container.frame.displayCanvas()

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


