import random
import sys
import time
from math import inf
from timeit import default_timer as timer
from copy import deepcopy

from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import *

from const import *
from main import *
from stone import Stone
from custom import Button_, ProgressBar, RoundRect


class Game(ttk.Frame):
    def __init__(self, container, width=GAME_WIDTH, height=GAME_HEIGHT):
        super().__init__(container)

        self.container = container
        self.width = width
        self.height = height
        self.pad = 50
        self.boardPad = 80
        self.hover = None

        self.container.title("Game")
        self.container.resizable(True, True)
        self.container.minsize(561, 561)

        centerPos = self.container.findCenter(winHeight=self.width, winWidth=self.height)
        self.container.geometry(f"{self.width}x{self.height}+{centerPos[0]}+{centerPos[1]}")

        self.displayCanvas()
        self.container.board.displayStones()

    def displayCanvas(self):
        self.canvas = Canvas(self, width=10000, height=10000, bg=self.container.background)
        self.canvas.pack(side=TOP, fill=BOTH, expand=NO)

        Button_(46, 8, self.canvas, name="back-button", text="MENU", font=(FONT, 20, "bold"),
                                   bg=self.container.background, fg=self.container.button_col)
        Button_(166, 8, self.canvas, name="pass-button", text="PASS", font=(FONT, 20, "bold"),
                                   bg=self.container.background, fg=self.container.button_col)
        Button_(286, 8, self.canvas, name="undo-button", text="UNDO", font=(FONT, 20, "bold"),
                                   bg=self.container.background, fg=self.container.button_col)
        Button_(406, 8, self.canvas, name="resign-button", text="RESIGN", font=(FONT, 20, "bold"),
                                   bg=self.container.background, fg=self.container.button_col)
        Button_(4150, 250, self.canvas, name="easteregg-button", text="?", font=(FONT, 20, "bold"),
                bg=self.container.background, fg=self.container.button_col)

        self.pack()

    def calcSquare(self, x, y):
        return int((x - self.pad - self.boardPad / 2) / self.boardPad), int(
            (y - self.pad - self.boardPad / 2) / self.boardPad)

    def displayBoard(self):
        bg = self.container.background
        board_line = self.container.board_line
        len = int(min(self.container.winfo_width(), self.container.winfo_height()))
        self.canvas.create_rectangle(self.pad, self.pad, len - self.pad, len - self.pad, fill=bg,
                                     outline=board_line)
        length = int(len - (2 * self.pad))
        self.boardPad = length / (self.container.board.size + 1)
        # draw board
        for row in range(self.container.board.size):
            self.canvas.create_line(self.pad + self.boardPad, self.pad + self.boardPad + row * self.boardPad,
                                    len - self.boardPad - self.pad, self.pad + self.boardPad + row * self.boardPad,
                                    fill=board_line)
            for col in range(self.container.board.size):
                self.canvas.create_line(self.pad + self.boardPad + col * self.boardPad, self.pad + self.boardPad,
                                        self.pad + self.boardPad + col * self.boardPad,len - self.pad - self.boardPad,
                                        fill=board_line)

                if self.container.board.size == 19 and row in (3, 9, 15) and col in (3, 9, 15):
                    self.canvas.create_oval(self.pad + self.boardPad + col * self.boardPad - 3,
                                            self.pad + self.boardPad + row * self.boardPad - 3,
                                            self.pad + self.boardPad + col * self.boardPad + 3,
                                            self.pad + self.boardPad + row * self.boardPad + 3,
                                            fill=board_line, outline=board_line)
                elif self.container.board.size == 13 and (row, col) in ((3, 3), (9, 3), (3, 9), (9, 9), (6, 6)):
                    self.canvas.create_oval(self.pad + self.boardPad + col * self.boardPad - 3,
                                            self.pad + self.boardPad + row * self.boardPad - 3,
                                            self.pad + self.boardPad + col * self.boardPad + 3,
                                            self.pad + self.boardPad + row * self.boardPad + 3,
                                            fill=board_line, outline=board_line)
                elif self.container.board.size == 9 and (row, col) in ((2, 2), (6, 2), (2, 6), (6, 6), (4, 4)):
                    self.canvas.create_oval(self.pad + self.boardPad + col * self.boardPad - 3,
                                            self.pad + self.boardPad + row * self.boardPad - 3,
                                            self.pad + self.boardPad + col * self.boardPad + 3,
                                            self.pad + self.boardPad + row * self.boardPad + 3,
                                            fill=board_line, outline=board_line)
        # draw stone counter
        RoundRect(self.canvas, len, self.pad , len + self.boardPad * 5, self.pad + self.boardPad * 10,
                  radius=self.boardPad / 2, fill="gray75")
        self.canvas.create_oval(len + self.boardPad * 0.5, self.pad + self.boardPad * 0.5,
                                len + self.boardPad * 0.5 + self.boardPad * 1.5,
                                self.pad + self.boardPad * 2, fill="black")
        self.canvas.create_oval(len + self.boardPad * 3, self.pad + self.boardPad * 0.5,
                                len + self.boardPad * 4.5,
                                self.pad + self.boardPad * 2, fill="white")
        fontSize = len//30
        self.canvas.create_text(len + self.boardPad * 0.5 + self.boardPad * 0.75, self.pad + self.boardPad * 2.5,
                                text=self.container.board.stonesCapturedByWhite, fill="black",
                                font=(FONT, fontSize, "bold"), justify="center")
        self.canvas.create_text(len + self.boardPad * 3 + self.boardPad * 0.75, self.pad + self.boardPad * 2.5,
                                text=self.container.board.stonesCapturedByBlack, fill="black",
                                font=(FONT, fontSize, "bold"), justify="center")

        self.container.board.displayStones()

    def displayEndgame(self, winner=None):
        len = int(min(self.container.winfo_width(), self.container.winfo_height()))
        fontsize = len // 9
        fontsize2 = len // 36

        black, white = self.container.board.calcInfluence()
        print(self.container.board.stonesCapturedByBlack)
        black, white = (str(black + self.container.board.stonesCapturedByBlack).zfill(3),
                        str(white + self.container.board.stonesCapturedByWhite).zfill(3))
        if winner == None:
            winner = "BLACK" if black > white else "WHITE" if white > black else "DRAW"

        RoundRect(self.canvas, len / 7, len / 2.5, len - len / 7, len - len / 2.5, fill="gray80", outline="black",
                  width=3, radius=50)
        if self.container.gamemode == "ai":
            self.container.frame.canvas.create_text(len / 2, len / 2.125,
                                                text="VICTORY" if winner == "BLACK" else "DEFEAT",
                                                font=(FONT, fontsize, "bold"), fill="black")
        else:
            if winner == "DRAW":
                self.container.frame.canvas.create_text(len / 2, len / 2.125,
                                                    text="DRAW", font=(FONT, fontsize, "bold"), fill="black")
            else:
                self.container.frame.canvas.create_text(len / 2, len / 2.125,
                                                        text=f"{winner} WINS", font=(FONT, int(fontsize / 1.5), "bold"),
                                                        fill="black")
        self.container.frame.canvas.create_text(len / 2, len / 1.75,
                                                text=f"WHITE {white} - {black}  BLACK",
                                                font=(FONT, fontsize2, "bold"), fill="black")

    def makeMoveAI(self):
        if len(self.container.board.history) == 0:
            return
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
            self.aiHard()

    def aiEasy(self):
        moves = self.container.board.calcMoves("black", "liberties")
        if moves == []:  # if no moves:
            moves = self.container.board.calcMoves("white", "liberties")
            if moves == []:  # if no moves:
                freeSpaces = self.container.board.calcMoves("black", "spaces")
                if freeSpaces == []:
                    self.container.board.endgame = True
                    self.container.board.calcInfluence()
                    self.container.board.displayTerretories()
                    self.container.frame.displayEndgame()
                else:
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
            if group[0] == "white" and len(group[1]) <= 1:  # defend
                groupsToDefend.append(group)
            elif group[0] == "black" and len(group[1]) <= 1:  # attack
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
        patternPos = self.container.board.checkPattern("black")
        if len(patternPos) != 0:
            print(f"Using pattern: {patternPos[0]}")
            move = patternPos[0]
            self.placeMove(move[0], move[1])
        else:
            if groupsToDefend != []:
                groupsToDefend.sort(key=len, reverse=True)
                print(f"Defending: {groupsToDefend[0]} at {groupsToDefend[0][1][0]}")
                self.placeMove(groupsToDefend[0][1][0][0], groupsToDefend[0][1][0][1])

            elif groupsToAttack != []:
                groupsToAttack.sort(key=len, reverse=True)
                print(f"Attacking: {groupsToAttack[0]} at {groupsToAttack[0][1][0]}")
                self.placeMove(groupsToAttack[0][1][0][0], groupsToAttack[0][1][0][1])

            else:
                self.aiEasy()

    def aiHard(self):
        # if group > 5 liberties = 1 >> check pattern: if pattern doesn't change liberties >> defend
        # else >> changing pattern
        progress = 0
        start = timer()
        board = self.container.board
        possibleMoves = board.calcValidMoves("white")
        patternPos = self.container.board.checkPattern("white")
        bestMove, bestLiberties = [], 0
        # patterns
        if patternPos != []:
            # filter patterns
            for pattern in patternPos:
                if pattern not in possibleMoves:
                    patternPos.remove(pattern)
            # eval patterns
            if patternPos != []:
                for pattern in patternPos:
                    self.container.board.evalMove(pattern, "white", 2, bestMove, bestLiberties)
        # check rest
        for move in possibleMoves:
            self.container.board.evalMove(move, "white", 3, bestMove, bestLiberties)
        # no best move
        if bestMove == []:
            self.aiEasy()
            return
        # place move
        self.placeMove(bestMove[0], bestMove[1])



        time1 = round(timer() - start, 2)
        print(f"time taken: {time1}s")
        print(f"")

    def minimax(self, board, depth, isMaximizer):

        res = board.getStoneDiff() # b - w >> ai likes negative
        if depth == 2: return res

        possibleMoves = board.calcValidMoves("black") if isMaximizer else (board.calcValidMoves("white"))

        if isMaximizer:
            bestScore = -inf
            for i in possibleMoves:
                pos = deepcopy(board.positions)
                board.positions[i[0]][i[1]] = Stone(col=i[0], row=i[1], color="black", boardPad=self.boardPad)
                board.processStones("black")
                score = self.minimax(board, depth + 1, False)
                board.positions = pos
                bestScore = max(score, bestScore)
            return bestScore

        else:
            bestScore = inf
            for i in possibleMoves:
                pos = deepcopy(board.positions)
                board.positions[i[0]][i[1]] = Stone(col=i[0], row=i[1], color="white", boardPad=self.boardPad)
                board.processStones("white")
                score = self.minimax(board, depth + 1, True)
                board.positions = pos
                bestScore = min(score, bestScore)
            return bestScore

    def placeMove(self, x, y):
        self.container.board.positions[x][y] = Stone(col=x, row=y, color="white", boardPad=self.boardPad)
        self.container.board.positions[x][y].draw(self.container.frame.canvas, "Game")
        self.container.board.processStones("white")
        self.container.board.processStones("white")
        self.container.board.archiveBoard()
        self.container.board.passCounter = 0

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

    def passConfirmation(self):
        out = tk.messagebox.askquestion('Player-Confirmation', 'Are you sure you want to pass your turn?\n'
                                                               'You will give 1 stone to your opponent.')
        if out == 'yes':
            return True
        else:
            return False

    def resignConfirmation(self):
        out = tk.messagebox.askquestion('Player-Confirmation', 'Are you sure you want to resign?\n'
                                                               'You will lose the game no matter the score.')
        if out == 'yes':
            return True
        else:
            return False

    def drawStone(self):
        pass