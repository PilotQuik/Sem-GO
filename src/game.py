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
from custom import Button_, RoundRect, Gif


class Game(ttk.Frame):
    def __init__(self, container, width=GAME_WIDTH, height=GAME_HEIGHT):
        super().__init__(container)

        self.container = container
        self.width = width
        self.height = height
        self.pad = 50
        self.boardPad = 80
        self.hover = None
        self.eggPlayed = False

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
        Button_(1900, 1000, self.canvas, name="easteregg-button", text="?", font=(FONT, 20, "bold"),
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
        RoundRect(self.canvas, len, self.pad , len + self.boardPad * 5, self.pad + self.boardPad * 3.25,
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
        black, white = (str(black + self.container.board.stonesCapturedByBlack).zfill(3),
                        str(white + self.container.board.stonesCapturedByWhite).zfill(3))
        if winner == None:
            winner = "BLACK" if black > white else "WHITE" if white > black else "DRAW"
        easteregg = winner

        RoundRect(self.canvas, len / 7, len / 2.5, len - len / 7, len - len / 2.5, fill="gray80", outline="black",
                  width=3, radius=50)
        if self.container.gamemode == "ai":
            self.container.frame.canvas.create_text(len / 2, len / 2.125,
                                                text="VICTORY" if winner == "BLACK" else "DEFEAT",
                                                font=(FONT, fontsize, "bold"), fill="black")
            easteregg = "VICTORY" if winner == "BLACK" else "DEFEAT"
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
        if self.container.easteregg and not self.eggPlayed:
            if easteregg in ["BLACK", "WHITE", "VICTORY"]:
                Gif(self.container.frame, len//2 - 240, len - 362, "assets/win_gif", 12, 3)
            elif easteregg in ["DEFEAT"]:
                Gif(self.container.frame, len // 2 - 240, len - 360, "assets/defeat_gif", 30, 3)
            else:
                Gif(self.container.frame, len // 2 - 250, len - 375, "assets/draw_gif", 12, 3)
            self.eggPlayed = True

    def makeMoveAI(self):
        if len(self.container.board.history) == 0:
            return

        if self.checkPass():
            self.container.board.stonesCapturedByBlack += 1
            self.container.board.aiPassCounter += 1
            self.container.board.passCounter += 1
            self.container.board.archiveBoard()
            self.passInformation()
            if self.container.board.passCounter == 2:
                self.container.board.endgame = True
                self.container.board.calcInfluence()
                self.container.board.displayTerretories()
                self.container.frame.displayEndgame()
        elif self.container.ai_level == "easy":
            start = timer()
            """
            Priorities:
            1   -   Place next to random black stone
            2   -   Place next to random white stone
            3   -   Place at random
            """
            self.aiEasy()
            print(f"Calcualtion-Time: {round(timer() - start, 4)}s\n-------------------------\n")

        elif self.container.ai_level == "medium":
            start = timer()
            """
            Priorities:
            1   -   Take groups with one liberty
            2   -   Match patterns
            3   -   Surround enemy groups with more than two liberties
            4   -   Easy AI
            """
            self.aiMedium()
            print(f"Calcualtion-Time: {round(timer() - start, 4)}s\n-------------------------\n")

        elif self.container.ai_level == "hard":
            start = timer()
            """
            Priorities:
            1   -   Take groups with one liberty
            2   -   Save own Groups with one liberty
            3   -   Forecast liberties of own groups with two liberties
            4   -   Match patterns
            5   -   Surround enemy groups with more than two liberties
            6   -   Easy AI
            """
            self.aiHard()
            print(f"Calcualtion-Time: {round(timer()-start, 4)}s\n-------------------------\n")

    def checkPass(self):
        board = self.container.board
        passCooldown = 20 if board.size == 9 else 40 if board.size == 13 else 60
        blackInf, whiteInf = board.calcInfluence()
        blackPoints, whitePoints = blackInf + board.stonesCapturedByBlack, whiteInf + board.stonesCapturedByWhite
        blackStones, whiteStones = 0, 0
        for col in range(board.size):
            for row in range(board.size):
                if isinstance(board.positions[col][row], Stone):
                    if board.positions[col][row].color == "black":
                        blackPoints += 1
                    if board.positions[col][row].color == "white":
                        whitePoints += 1
        if board.passCounter == 1:
            if blackPoints < whitePoints:
                print("pass")
                return True
        if (blackPoints < whitePoints * 0.25 and len(board.history) > board.size * board.size * 0.5 +
                passCooldown * board.aiPassCounter):
            return True
        if (whitePoints < blackPoints * 0.25 and len(board.history) > board.size * board.size * 0.5 +
                passCooldown * board.aiPassCounter):
            return True
        return False

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
                    return
                else:
                    move = freeSpaces[random.randint(0, len(freeSpaces) - 1)]
                    self.placeMove(move[0], move[1])

            else:
                move = moves[random.randint(0, len(moves) - 1)]
                self.placeMove(move[0], move[1])

        else:
            move = moves[random.randint(0, len(moves) - 1)]
            self.placeMove(move[0], move[1])

    def aiMedium(self):
        board = self.container.board
        patternPos = board.checkPattern("white")
        groups = board.getGroups()

        bestMove = None
        # 1 - Take groups with one liberty
        targetGroups = []
        for group in groups:
            if len(group[1]) == 1 and group[0] == "black":
                targetGroups.append(group)
        if targetGroups != []:
            bestGroup, bestSize = [], 0
            for group in targetGroups:
                if not self.container.board.checkMove(group[1][0][0], group[1][0][1], "white"):
                    targetGroups.remove(group)
                    continue
                elif len(group[2]) > bestSize:
                    bestGroup, bestSize = group, len(group[2])
            if bestGroup != []:
                bestMove = bestGroup[1][0]
                self.placeMove(bestMove[0], bestMove[1])
                return

        # 2 - Match patterns
        if patternPos != []:
            bestPattern, bestLiberties = [], 0
            for pattern in patternPos:
                if not self.container.board.checkMove(pattern[0], pattern[1], "white"):
                    patternPos.remove(pattern)
                    continue
                lib = board.libertieForecast(pattern[0], pattern[1], "white")
                if lib > bestLiberties:
                    bestPattern, bestLiberties = pattern, lib
            if bestPattern != []:
                bestMove = bestPattern[1]
                print(bestMove)
                self.placeMove(bestPattern[0], bestPattern[1])
                return

        # 3 - Surround enemy groups with more than two liberties
        targetGroups = []
        for group in groups:
            if len(group[1]) == 1 and group[0] == "black":
                targetGroups.append(group)
        if targetGroups != []:
            bestGroup, bestSize = [], 100
            for group in targetGroups:
                if not self.container.board.checkMove(group[1][0][0], group[1][0][1], "white"):
                    targetGroups.remove(group)
                    continue
                elif len(group[1]) < bestSize:
                    bestGroup, bestSize = group, len(group[1])
            if bestGroup != []:
                bestMove = bestGroup[1][0]
                self.placeMove(bestMove[0], bestMove[1])
                return

        # 4 - Easy AI
        self.aiEasy()
        return

    def aiHard(self):
        board = self.container.board
        patternPos = board.checkPattern("white")
        groups = board.getGroups()

        bestMove = None
        # 1   -   Take groups with one liberty
        targetGroups = []
        for group in groups:
            if len(group[1]) == 1 and group[0] == "black":
                targetGroups.append(group)
        if targetGroups != []:
            bestGroup, bestSize = [], 0
            for group in targetGroups:
                if not self.container.board.checkMove(group[1][0][0], group[1][0][1], "white"):
                    targetGroups.remove(group)
                    continue
                elif len(group[2]) > bestSize:
                    bestGroup, bestSize = group, len(group[2])
            if bestGroup != []:
                bestMove = bestGroup[1][0]
                self.placeMove(bestMove[0], bestMove[1])
                return

        # 2 - Save own Groups with one liberty
        targetGroups = []
        for group in groups:
            if len(group[1]) == 1 and group[0] == "white":
                targetGroups.append(group)
        if targetGroups != []:
            bestGroup, bestLib = [], 0
            for group in targetGroups:
                if not self.container.board.checkMove(group[1][0][0], group[1][0][1], "white"):
                    targetGroups.remove(group)
                    continue
                lib = board.libertieForecast(group[1][0][0], group[1][0][1], "white")
                if lib <= 2:
                    targetGroups.remove(group)
                    continue
                elif len(group[2]) > bestLib:
                    bestGroup, bestLib = group, lib
            if bestGroup != []:
                bestMove = bestGroup[1][0]
                self.placeMove(bestMove[0], bestMove[1])
                return

        # 3 - Forecast liberties of own groups with two liberties
        targetGroups = []
        for group in groups:
            if len(group[1]) == 2 and group[0] == "black":
                targetGroups.append(group)
        if targetGroups != []:
            bestPos, bestLiberties = [], 0
            for group in targetGroups:
                for pos in group[1]:
                    if not self.container.board.checkMove(pos[0], pos[1], "white"):
                        group[1].remove(pos)
                        continue
                    lib = board.libertieForecast(pos[0], pos[1], "white")
                    if lib > bestLiberties:
                        bestPos, bestLiberties = pos, lib
            if bestPos != []:
                bestMove = bestPos
                self.placeMove(bestMove[0], bestMove[1])
                return

        # 4 - Match patterns
        if patternPos != []:
            bestPattern, bestLiberties = [], 0
            for pattern in patternPos:
                if not self.container.board.checkMove(pattern[0], pattern[1], "white"):
                    patternPos.remove(pattern)
                    continue
                lib = board.libertieForecast(pattern[0], pattern[1], "white")
                if lib > bestLiberties:
                    bestPattern, bestLiberties = pattern, lib
            if bestPattern != []:
                bestMove = bestPattern[1]
                print(bestMove)
                self.placeMove(bestPattern[0], bestPattern[1])
                return

        # 5 - Surround enemy groups with more than two liberties
        targetGroups = []
        for group in groups:
            if len(group[1]) == 1 and group[0] == "black":
                targetGroups.append(group)
        if targetGroups != []:
            bestGroup, bestSize = [], 100
            for group in targetGroups:
                if not self.container.board.checkMove(group[1][0][0], group[1][0][1], "white"):
                    targetGroups.remove(group)
                    continue
                elif len(group[1]) < bestSize:
                    bestGroup, bestSize = group, len(group[1])
            if bestGroup != []:
                bestMove = bestGroup[1][0]
                self.placeMove(bestMove[0], bestMove[1])
                return

        # 6 - Easy AI
        self.aiEasy()
        return

    def placeMove(self, x, y):
        self.container.board.positions[x][y] = Stone(col=x, row=y, color="white", boardPad=self.boardPad)
        self.container.board.positions[x][y].draw(self.container.frame.canvas, "Game")
        self.container.board.processStones("white")
        self.container.board.archiveBoard()
        self.container.board.passCounter = 0
        print("Move:", x, y)

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
        out = tk.messagebox.askquestion('Player-Confirmation',
                                        'Are you sure you want to pass your turn?\n'
                                                'You will give 1 stone to your opponent.')
        if out == 'yes':
            return True
        else:
            return False

    def resignConfirmation(self):
        out = tk.messagebox.askquestion('Player-Confirmation',
                                        'Are you sure you want to resign?\n'
                                                'You will lose the game no matter the score.')
        if out == 'yes':
            return True
        else:
            return False

    def passInformation(self):
        out = tk.messagebox.showwarning('Player-Confirmation',
                                        'The AI has passed its turn and given you one stone.')
