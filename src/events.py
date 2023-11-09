import webbrowser
import os

from tkinter import *

from const import *
from main import *
from game import Game
from opt import Opt
from stone import Stone

import os

class Event:
    def __init__(self, container):
        self.container = container

    def mouse1(self, event = NONE):
        frame = self.container.frame
        len = int(min(self.container.winfo_width(), self.container.winfo_height()))
        length = int(len - 100)
        boardPad = length / (self.container.board.size + 1)
        #print(int(event.x), int(event.y), event.widget)

        if isinstance(self.container.frame, Menu): #--------------------------------------------------------------------
            if str(event.widget).split(".")[-1] == "play-button":
                self.container.switchFrame(Game, width=GAME_WIDTH, height=GAME_HEIGHT)
            elif str(event.widget).split(".")[-1] == "opt-button":
                self.container.switchFrame(Opt, width=OPT_WIDTH, height=OPT_HEIGHT)
            elif str(event.widget).split(".")[-1] == "quit-button":
                self.container.board.saveBoard()
                self.container.destroy()
            elif str(event.widget).split(".")[-1] == "rules-button":

                try: #default
                    webbrowser.get().open_new_tab(f"file:///{os.getcwd()}/assets/rules.html")
                except:
                    print("could not open default browser")
                    try: #notepad
                        os.system("notepad.exe assets/rules.md")
                    except:
                        print("unable to display rules")

            elif str(event.widget).split(".")[-1] == "load-button":
                self.container.board = self.container.board.loadBoard()
                self.container.frame.displayBoard()

        elif isinstance(self.container.frame, Game): #------------------------------------------------------------------
            # top bar
            if str(event.widget).split(".")[-1] == "back-button":
                self.container.switchFrame(Menu, width=MENU_WIDTH, height=MENU_HEIGHT)
            elif str(event.widget).split(".")[-1] == "pass-button":
                if self.container.frame.passConfirmation():
                    if self.container.board.currentPlayer == "white":
                        self.container.board.stonesCapturedByBlack += 1
                        self.container.board.currentPlayer = "black"
                        self.container.board.archiveBoard("white")
                    else:
                        self.container.board.stonesCapturedByWhite += 1
                        self.container.board.currentPlayer = "white"
                        self.container.board.archiveBoard("black")
                    self.container.refresh()
                    self.container.board.passCounter += 1
                    if self.container.board.passCounter == 2:
                        print("endgame evaluation")
            elif str(event.widget).split(".")[-1] == "undo-button":
                self.container.board.undoMove()
            elif str(event.widget).split(".")[-1] == "resign-button":
                print("resign") # evaluate points but make current player lose
            elif str(event.widget).split(".")[-1] == "easteregg-button":
                print("easteregg")
            # player move
            if str(event.widget).split(".")[-1] == "!canvas":
                x, y = self.container.frame.calcSquare(event.x, event.y)
                pad = self.container.frame.boardPad / 2 + self.container.frame.pad
                if event.x <= self.container.winfo_width() - pad and event.y <= self.container.winfo_height() - pad and\
                        event.x >= pad and event.y >= pad:
                    color = self.container.board.currentPlayer
                    pos = self.container.board.positions[x][y]
                    # check move validity
                    if self.container.board.checkMove(x, y, color):
                        self.container.board.positions[x][y] = Stone(col=x, row=y, color=color, boardPad=boardPad)
                        self.container.board.positions[x][y].draw(self.container.frame.canvas, "Game")
                        self.container.board.processStones(color)
                        self.container.board.archiveBoard([x, y])
                        self.container.board.passCounter = 0
                        if self.container.gamemode == "player":
                            self.container.board.currentPlayer = "black" if color == "white" else "white"
                        elif self.container.gamemode == "ai":
                            self.container.frame.makeMoveAI()

        elif isinstance(self.container.frame, Opt): #-------------------------------------------------------------------
            if str(event.widget).split(".")[-1] == "back-button":
                self.container.switchFrame(Menu, width=MENU_WIDTH, height=MENU_HEIGHT)
            elif str(event.widget).split(".")[-1] == "play-button":
                self.container.switchFrame(Game, width=GAME_WIDTH, height=GAME_HEIGHT)
            # gamemode
            elif str(event.widget).split(".")[-1] == "vs-player-button":
                self.container.gamemode = "player"
                self.container.frame.displayCanvas()
                if self.container.aiFirst:
                    self.container.aiFirst = False
                    self.container.board.currentPlayer = "black"
            elif str(event.widget).split(".")[-1] == "vs-ai-button":
                self.container.gamemode = "ai"
                self.container.frame.displayCanvas()
                if self.container.board.currentPlayer == "white":
                    self.container.aiFirst = True
                    self.container.board.currentPlayer = "black"
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
                self.container.board.__init__(self.container, 9)
                self.container.frame.displayCanvas()
            elif str(event.widget).split(".")[-1] == "13x13-button":
                self.container.board.__init__(self.container, 13)
                self.container.frame.displayCanvas()
            elif str(event.widget).split(".")[-1] == "19x19-button":
                self.container.board.__init__(self.container, 19)
                self.container.frame.displayCanvas()
            # theme
            elif str(event.widget).split(".")[-1] == "classic-button":
                self.container.theme = "classic"
                self.container.background = BACKGROUND
                self.container.button_col = BUTTON_COL
                self.container.button_col_clicked = BUTTON_COL_CLICKED
                self.container.button_col_selected = BUTTON_COL_SELECTED
                self.container.board_col = BOARD_COL
                self.container.board_line = BOARD_LINE
                self.container.hover_b = HOVER_B
                self.container.hover_w = HOVER_W
                self.container.frame.displayCanvas()
            elif str(event.widget).split(".")[-1] == "light-button":
                self.container.theme = "light"
                self.container.background = BACKGROUND_LIGHT
                self.container.button_col = BUTTON_COL_LIGHT
                self.container.button_col_clicked = BUTTON_COL_CLICKED_LIGHT
                self.container.button_col_selected = BUTTON_COL_SELECTED_LIGHT
                self.container.board_col = BOARD_COL_LIGHT
                self.container.board_line = BOARD_LINE_LIGHT
                self.container.hover_b = HOVER_B_LIGHT
                self.container.hover_w = HOVER_W_LIGHT
                self.container.frame.displayCanvas()
            elif str(event.widget).split(".")[-1] == "dark-button":
                self.container.theme = "dark"
                self.container.background = BACKGROUND_DARK
                self.container.button_col = BUTTON_COL_DARK
                self.container.button_col_clicked = BUTTON_COL_CLICKED_DARK
                self.container.button_col_selected = BUTTON_COL_SELECTED_DARK
                self.container.board_col = BOARD_COL_DARK
                self.container.board_line = BOARD_LINE_DARK
                self.container.hover_b = HOVER_B_DARK
                self.container.hover_w = HOVER_W_DARK
                self.container.frame.displayCanvas()

    def mouse3(self, event=NONE):
        frame = self.container.frame
        len = int(min(self.container.winfo_width(), self.container.winfo_height()))
        length = int(len - 100)
        boardPad = length / (self.container.board.size + 1)
        if isinstance(self.container.frame, Game):
            if str(event.widget).split(".")[-1] == "!canvas":
                x, y = self.container.frame.calcSquare(event.x, event.y)
                pad = self.container.frame.boardPad / 2 + self.container.frame.pad
                if event.x <= self.container.winfo_width() - pad and event.y <= self.container.winfo_height() - pad and \
                        event.x >= pad and event.y >= pad:
                    self.container.board.calcInfluence()
                    self.container.board.displayTerretories()
                    self.container.frame.displayEndgame()


    def onHoverEnter(self, event=None):
        if "-button" in str(event.widget).split(".")[-1]:
            event.widget.config(fg=self.container.button_col_clicked)


    def onHoverLeave(self, event=None):
        if "-button" in str(event.widget).split(".")[-1]:
            event.widget.config(fg=self.container.button_col)

    def motion(self, event=None):
        if isinstance(self.container.frame, Game):
            x, y = self.container.frame.calcSquare(event.x, event.y)
            pad = self.container.frame.boardPad / 2 + self.container.frame.pad
            if (event.x <= self.container.winfo_width() - pad and event.y <= self.container.winfo_height() - pad and
                    event.x >= pad and event.y >= pad):
                if x in range(0, self.container.board.size) and y in range(0, self.container.board.size):
                    if not isinstance(self.container.board.positions[x][y], Stone):
                        self.container.frame.drawHover(x, y, False)
                    else: self.container.frame.drawHover(x, y, True)
            else: self.container.frame.drawHover(x, y, True)

    def config(self, event=None):
        #print(event.widget, event.width, event.height)
        #print(self.container.winfo_width(), self.container.winfo_height())
        if isinstance(event.widget, Canvas) and isinstance(self.container.frame, Game):
            if int(self.container.winfo_width()) == int(event.width) and int(self.container.winfo_height()) == int(event.height):
                self.container.frame.canvas.delete("all")
                self.container.frame.displayBoard()
                self.container.board.displayStones()
