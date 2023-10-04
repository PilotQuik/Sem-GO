import random
import time

from tkinter import ttk
from tkinter import *

from const import *
from main import *
from stone import Stone
from custom import Button_


class Game(ttk.Frame):
    def __init__(self, container, width=GAME_WIDTH, height=GAME_HEIGHT):
        super().__init__(container)

        self.container = container
        self.width = width
        self.height = height
        self.pad = 50
        self.boardPad = 80
        self.hover = None

        self.container.title("Menu")
        self.container.resizable(True, True)
        self.container.minsize(500, 500)

        centerPos = self.container.findCenter(winHeight=self.width, winWidth=self.height)
        self.container.geometry(f"{self.width}x{self.height}+{centerPos[0]}+{centerPos[1]}")

        self.displayCanvas()
        self.container.board.displayStones()

    def displayCanvas(self):
        self.canvas = Canvas(self, width=10000, height=10000, bg='white')
        self.canvas.pack(side=TOP, fill=BOTH, expand=NO)

        Button_(3, 5, self.canvas, name="back-button", text="<<",
                font=(FONT, 25, "bold"))
        self.pack()

    def calcSquare(self, x, y):
        return int((x - self.pad - self.boardPad / 2) / self.boardPad), int(
            (y - self.pad - self.boardPad / 2) / self.boardPad)

    def displayBoard(self):
        len = int(min(self.container.winfo_width(), self.container.winfo_height()))
        self.canvas.create_rectangle(self.pad, self.pad, len - self.pad, len - self.pad, fill="#c9833c",
                                     outline="black")
        length = int(len - (2 * self.pad))
        self.boardPad = length / (self.container.board.size + 1)
        # draw board
        for row in range(self.container.board.size):
            self.canvas.create_line(self.pad + self.boardPad, self.pad + self.boardPad + row * self.boardPad,
                                    len - self.boardPad - self.pad, self.pad + self.boardPad + row * self.boardPad)
            for col in range(self.container.board.size):
                self.canvas.create_line(self.pad + self.boardPad + col * self.boardPad, self.pad + self.boardPad,
                                        self.pad + self.boardPad + col * self.boardPad,len - self.pad - self.boardPad)

                if self.container.board.size == 19 and row in (3, 9, 15) and col in (3, 9, 15):
                    self.canvas.create_oval(self.pad + self.boardPad + col * self.boardPad - 3,
                                            self.pad + self.boardPad + row * self.boardPad - 3,
                                            self.pad + self.boardPad + col * self.boardPad + 3,
                                            self.pad + self.boardPad + row * self.boardPad + 3, fill="black")
                elif self.container.board.size == 13 and (row, col) in ((3, 3), (9, 3), (3, 9), (9, 9), (6, 6)):
                    self.canvas.create_oval(self.pad + self.boardPad + col * self.boardPad - 3,
                                            self.pad + self.boardPad + row * self.boardPad - 3,
                                            self.pad + self.boardPad + col * self.boardPad + 3,
                                            self.pad + self.boardPad + row * self.boardPad + 3, fill="black")
                elif self.container.board.size == 9 and (row, col) in ((2, 2), (6, 2), (2, 6), (6, 6), (4, 4)):
                    self.canvas.create_oval(self.pad + self.boardPad + col * self.boardPad - 3,
                                            self.pad + self.boardPad + row * self.boardPad - 3,
                                            self.pad + self.boardPad + col * self.boardPad + 3,
                                            self.pad + self.boardPad + row * self.boardPad + 3, fill="black")

        self.container.board.displayStones()

    def makeMoveAI(self):
        if self.container.ai_level == "easy":
            self.aiEasy()

        elif self.container.ai_level == "medium":
            """
            Priorities:
            1   -   Take more than would be lost
            2   -   Preservation
            3   -   Offence
            """
            self.aiMedium()

        elif self.container.ai_level == "hard":
            pass

    def aiEasy(self):
        moves = self.container.board.calcValidMoves("black", "liberties")
        if moves == []:  # if no moves:
            moves = self.container.board.calcValidMoves("white", "liberties")
            if moves == []:  # if no moves:
                freeSpaces = self.container.board.calcValidMoves("black", "spaces")
                move = freeSpaces[random.randint(0, len(freeSpaces) - 1)]
                self.placeMove(move[0], move[1])

            else:
                move = moves[random.randint(0, len(moves) - 1)]
                self.placeMove(move[0], move[1])

        else:
            move = moves[random.randint(0, len(moves) - 1)]
            self.placeMove(move[0], move[1])

    def aiMedium(self): # check move validity
        board = self.container.board
        groups = self.container.board.getGroups()
        groupsToDefend = []
        groupsToAttack = []
        # GET GROUPS ---------------------------------------------------------------------------------------------------
        for group in groups:
            if group[0] == "white" and len(group[1]) <= 2:  # defend
                groupsToDefend.append(group)
            elif group[0] == "black" and len(group[1]) <= 2:  # attack
                groupsToAttack.append(group)
        patternPos = self.container.board.checkPattern("white")
        # FILTER MOVES -------------------------------------------------------------------------------------------------
        for group in groupsToDefend:
            for pos in group[1]:
                x, y = pos[0], pos[1]
                space = self.container.board.positions[x][y]
                self.container.board.positions[x][y] = Stone(col=x, row=y, color="white", boardPad=self.boardPad)
                if board.positions[x][y] == 99 or not board.processStones("white", [pos[0], pos[1]]):
                    group[1].remove(pos)
                    print("--purged in Defend")
                self.container.board.positions[x][y] = space
            if len(group[1]) == 0: groupsToDefend.remove(group)
        for group in groupsToAttack:
            for pos in group[1]:
                x, y = pos[0], pos[1]
                space = self.container.board.positions[x][y]
                self.container.board.positions[x][y] = Stone(col=x, row=y, color="white", boardPad=self.boardPad)
                if board.positions[pos[0]][pos[1]] == 99 or not board.processStones("white", [pos[0], pos[1]]):
                    group[1].remove(pos)
                    print("--purged in Attack")
                self.container.board.positions[x][y] = space
            if len(group[1]) == 0: groupsToAttack.remove(group)
        for pos in patternPos:
            x, y = pos[0], pos[1]
            space = self.container.board.positions[x][y]
            self.container.board.positions[x][y] = Stone(col=x, row=y, color="white", boardPad=self.boardPad)
            if board.positions[pos[0]][pos[1]] == 99 or not board.processStones("white", [pos[0], pos[1]]):
                patternPos.remove(pos)
                print("--purged in patternPos")
            self.container.board.positions[x][y] = space

        # MAKE MOVE ----------------------------------------------------------------------------------------------------
        if groupsToDefend != []:
            groupsToDefend.sort(key=len, reverse=True)
            print(f"Defending: {groupsToDefend[0]} at {groupsToDefend[0][1][0]}")
            self.placeMove(groupsToDefend[0][1][0][0], groupsToDefend[0][1][0][1])

        elif groupsToAttack != []:
            groupsToAttack.sort(key=len, reverse=True)
            print(f"Attacking: {groupsToAttack[0]} at {groupsToAttack[0][1][0]}")
            self.placeMove(groupsToAttack[0][1][0][0], groupsToAttack[0][1][0][1])

        else:
            patternPos = self.container.board.checkPattern("black")
            if len(patternPos) != 0:
                print(f"Using pattern: {patternPos[0]}")
                move = patternPos[0]
                self.placeMove(move[0], move[1])
            else:
                self.aiEasy()

    def placeMove(self, x, y):
            self.container.board.positions[x][y] = Stone(col=x, row=y, color="white", boardPad=self.boardPad)
            self.container.board.positions[x][y].draw(self.container.frame.canvas, "Game")
            self.container.board.processStones("white")
            self.container.board.processStones("white")

    def drawHover(self, x, y, delete):
        color = self.container.board.currentPlayer
        self.canvas.delete(self.hover)
        if delete: self.canvas.delete(self.hover)
        elif color == "white" and self.container.gamemode == "player":
            self.hover = self.canvas.create_oval(
            50 + self.boardPad + x * self.boardPad - self.boardPad / 2.5,
            50 + self.boardPad + y * self.boardPad - self.boardPad / 2.5,
            50 + self.boardPad + x * self.boardPad + self.boardPad / 2.5,
            50 + self.boardPad + y * self.boardPad + self.boardPad / 2.5,
            fill=HOVER_W)
        elif color == "black":
            self.hover = self.canvas.create_oval(
                50 + self.boardPad + x * self.boardPad - self.boardPad / 2.5,
                50 + self.boardPad + y * self.boardPad - self.boardPad / 2.5,
                50 + self.boardPad + x * self.boardPad + self.boardPad / 2.5,
                50 + self.boardPad + y * self.boardPad + self.boardPad / 2.5,
                fill=HOVER_B)

    def drawStone(self):
        pass