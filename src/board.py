import pickle
import time
from copy import deepcopy

from stone import Stone
from const import *
from custom import RoundRect

class Board:
    def __init__(self, container, size=9):
        self.container = container
        self.size = size
        self.positions = [[0 for row in range(self.size)] for col in range(self.size)]
        self.validMoves = []
        self.currentPlayer = "black"
        self.stonesCapturedByBlack = 0
        self.stonesCapturedByWhite = 0
        self.history = []
        self.archiveBoard()
        self.passCounter = 0
        self.aiPassCounter = 0
        self.endgame = False

        self.influence = []

        len = int(min(self.container.winfo_width(), self.container.winfo_height()))
        length = int(len - 100)
        self.boardPad = length / (self.size + 1)

    def getStoneDiff(self):
        black, white = 0, 0
        for col in range(self.size):
            for row in range(self.size):
                if isinstance(self.positions[col][row], Stone):
                    if self.positions[col][row].color == "white":
                        white += 1
                    else: black += 1
        return black - white

    def calcInfluence(self):
        # black stone = 50, white stone = -50
        self.influence = [[0 for row in range(self.size)] for col in range(self.size)]
        influence = deepcopy(self.influence)

        for col in range(self.size):
            for row in range(self.size):
                pos = self.positions[col][row]
                if isinstance(pos, Stone):
                    self.influence[col][row] = 50 if pos.color == "black" else -50

        for i in range(4):
            for col in range(self.size):
                for row in range(self.size):
                    pos = self.influence[col][row]
                    f = 1 if pos > 0 else -1
                    if pos != 0:

                        if col - 1 >= 0:
                            influence[col - 1][row] += f
                        if col + 1 < self.size:
                            influence[col + 1][row] += f
                        if row - 1 >= 0:
                            influence[col][row - 1] += f
                        if row + 1 < self.size:
                            influence[col][row + 1] += f
            self.influence = [[sum(x) for x in zip(self.influence[i], influence[i])] for i in range(self.size)]

        # count -------------------------------------------------
        i, j = 0, 0
        for col in range(self.size):
            for row in range(self.size):
                if self.influence[col][row] > 0:
                    i += 1
                elif self.influence[col][row] < 0:
                    j += 1
        return i, j

    def calcTerretoriesFromInfluence(self):
        influenceMap = deepcopy(self.influence)
        terretories = []
        for col in range(self.size):
            for row in range(self.size):
                pos = influenceMap[col][row]
                if pos != 0:
                    if pos < 0:
                        terretories.append(["white", self.getTerretory(influenceMap, col, row, 1)])
                    else:
                        terretories.append(["black", self.getTerretory(influenceMap, col, row, -1)])
        return terretories
    def getTerretory(self, map, col, row, neg, terretory=[]):
        pos = map[col][row]
        if pos != 0 and pos * neg < 0:
            map[col][row] = 0
            terretory.append([col, row])

            if row - 1 >= 0:
                terretory = self.getTerretory(map, col, row - 1, neg, terretory)  # oben
            if row + 1 < self.size:
                terretory = self.getTerretory(map, col, row + 1, neg, terretory)  # unten
            if col - 1 >= 0:
                terretory = self.getTerretory(map, col - 1, row, neg, terretory)  # links
            if col + 1 < self.size:
                terretory = self.getTerretory(map, col + 1, row, neg, terretory)  # rechts

        return terretory

    def calcMoves(self, activePlayer, *filter):
        if "liberties" in filter:
            libs = []
            # resetting groups and stone markers
            for col in range(self.size):
                for row in range(self.size):
                    pos = self.positions[col][row]
                    neighbours = 0
                    isLib = False
                    if not isinstance(pos, Stone):
                        if row - 1 >= 0:
                            posNord = self.positions[col][row - 1]
                            if isinstance(posNord, Stone):
                                neighbours += 1
                                if not posNord.color == activePlayer:
                                    isLib = True
                        else: neighbours += 1
                        if row + 1 < self.size:
                            posSüd = self.positions[col][row + 1]
                            if isinstance(posSüd, Stone):
                                neighbours += 1
                                if not posSüd.color == activePlayer:
                                    isLib = True
                        else: neighbours += 1
                        if col - 1 >= 0:
                            posWest = self.positions[col - 1][row]
                            if isinstance(posWest, Stone):
                                neighbours += 1
                                if not posWest.color == activePlayer:
                                    isLib = True
                        else: neighbours += 1
                        if col + 1 < self.size:
                            posOst = self.positions[col + 1][row]
                            if isinstance(posOst, Stone):
                                neighbours += 1
                                if not posOst.color == activePlayer:
                                    isLib = True
                        else: neighbours += 1
                        if not neighbours == 4 and isLib: libs.append([col, row]); #print("added ", col, row)
            return libs
        if "spaces" in filter:
            spaces = []
            for col in range(self.size):
                for row in range(self.size):
                    pos = self.positions[col][row]
                    neighbours = 0
                    if not isinstance(pos, Stone):
                        if row - 1 >= 0:
                            posNord = self.positions[col][row - 1]
                            if isinstance(posNord, Stone):
                                neighbours += 1
                        else: neighbours += 1
                        if row + 1 < self.size:
                            posSüd = self.positions[col][row + 1]
                            if isinstance(posSüd, Stone):
                                neighbours += 1
                        else: neighbours += 1
                        if col - 1 >= 0:
                            posWest = self.positions[col - 1][row]
                            if isinstance(posWest, Stone):
                                neighbours += 1
                        else: neighbours += 1
                        if col + 1 < self.size:
                            posOst = self.positions[col + 1][row]
                            if isinstance(posOst, Stone):
                                neighbours += 1
                        else: neighbours += 1
                        if not neighbours == 4: spaces.append([col, row]); print("added ", col, row)
            return spaces

    def checkMove(self, col, row, colorToMove):
        board = self.positions
        pos = deepcopy(board[col][row])

        if isinstance(pos, Stone) or pos == 99:
            return False

        board[col][row] = Stone(col, row, colorToMove, self.boardPad)
        if not self.processStones(colorToMove, checkMove=[col, row]):
            board[col][row] = pos
            return False

        board[col][row] = pos
        return True

    def getValidMoves(self, colorToMove):
        validMoves = []
        for col in range(self.size):
            for row in range(self.size):
                if self.checkMove(col, row, colorToMove):
                    validMoves.append([col, row])
        return validMoves

    def getGroups(self):
        # [color, liberties, [positions]]
        groups = []
        # RESET --------------------------------------------------------------------------------------------------------
        for col in range(self.size):
            for row in range(self.size):
                pos = deepcopy(self.positions[col][row])
                if isinstance(pos, Stone) and self.positions[col][row].marked == True:
                    self.positions[col][row].marked = False
        # PROCESS ------------------------------------------------------------------------------------------------------
        for col in range(self.size):
            for row in range(self.size):
                pos = deepcopy(self.positions[col][row])
                if isinstance(pos, Stone) and not self.positions[col][row].marked:
                    # --------------------------------count
                    group, liberties = self.countLibertiesAndGroups(col, row, self.positions[col][row].color, group=[], liberties=0)
                    # --------------------------------get liberties
                    liberties = self.getLibertiesFromGroup(group)
                    groups.append([self.positions[col][row].color, liberties, group])
        return groups

    def processStones(self, color, checkMove=None):
        stonesToDeleteW = []
        stonesToDeleteB = []
        # RESET --------------------------------------------------------------------------------------------------------
        for col in range(self.size):
            for row in range(self.size):
                pos = self.positions[col][row]
                if isinstance(pos, Stone) and pos.marked == True:
                    pos.marked = False
                elif pos == 99:
                    self.positions[col][row] = 0
        # CHECK --------------------------------------------------------------------------------------------------------
        if checkMove != None:
            pos = self.positions[checkMove[0]][checkMove[1]]
            # --------------------------------count
            checkGroup, checkLiberties = self.countLibertiesAndGroups(checkMove[0], checkMove[1], pos.color, group=[], liberties=0)
        # PROCESS ------------------------------------------------------------------------------------------------------
        for col in range(self.size):
            for row in range(self.size):
                pos = self.positions[col][row]
                if isinstance(pos, Stone) and not pos.marked:
                    # --------------------------------count
                    group, liberties = self.countLibertiesAndGroups(col, row, pos.color, group=[], liberties=0)
                    if liberties == 0:
                        for stone in group:
                            stonesToDeleteW.append(stone) if (self.positions[col][row].color
                                                              == "white") else stonesToDeleteB.append(stone)
        # RESET --------------------------------------------------------------------------------------------------------
        for col in range(self.size):
            for row in range(self.size):
                pos = self.positions[col][row]
                if isinstance(pos, Stone) and pos.marked == True:
                    pos.marked = False
        # DELETE -------------------------------------------------------------------------------------------------------
        if checkMove == None:
            for pos in stonesToDeleteB if color == "white" else stonesToDeleteW:
                self.positions[pos[0]][pos[1]] = 99
                if color == "white":
                    self.stonesCapturedByWhite += 1
                else: self.stonesCapturedByBlack += 1
                self.container.refresh()
        else:
            toDelete = stonesToDeleteB if color == "white" else stonesToDeleteW
            if checkLiberties == 0 and toDelete == []:
                return False # not valid
            else: return True # valid

    def checkPattern(self, color):
        matches = []
        _color = "white" if color == "black" else "black"
        for col in range(self.size):
            for row in range(self.size):
                if isinstance(self.positions[col][row], Stone):
                    if self.positions[col][row].color == _color:
                        for pattern in PATTERNS:
                            match = 0
                            for ownColor in pattern[0]:
                                if (col + ownColor[0] in range(0, self.size) and row + ownColor[1] in range(0, self.size)
                                        and isinstance(self.positions[col + ownColor[0]][row + ownColor[1]], Stone)
                                        and self.positions[col + ownColor[0]][row + ownColor[1]].color == color):
                                    match += 1
                                elif (col + ownColor[0] in [-1, self.size] or row + ownColor[1]
                                    in [-1, self.size]):
                                    match += 1
                            if (col + pattern[1][0] in range(0, self.size) and row + pattern[1][1] in range(0, self.size)
                                    and not isinstance(self.positions[col + pattern[1][0]][row + pattern[1][1]], Stone)):
                                match += 1
                            if match == 3 and [col + pattern[1][0], row + pattern[1][1]] not in matches:
                                matches.append([col + pattern[1][0], row + pattern[1][1]])
        return matches



    def getLibertiesFromGroup(self, group):
        liberties = []
        for pos in group:
            col, row = pos[0], pos[1]
            if row - 1 >= 0:
                if not isinstance(self.positions[col][row - 1], Stone) and pos not in liberties:
                    liberties.append([col, row - 1])
            if row + 1 < self.size:
                if not isinstance(self.positions[col][row + 1], Stone) and pos not in liberties:
                    liberties.append([col, row + 1])
            if col - 1 >= 0:
                if not isinstance(self.positions[col - 1][row], Stone) and pos not in liberties:
                    liberties.append([col - 1, row])
            if col + 1 < self.size:
                if not isinstance(self.positions[col + 1][row], Stone) and pos not in liberties:
                    liberties.append([col + 1, row])
        return liberties

    def countLibertiesAndGroups(self, col, row, color, group, liberties):
        piece = self.positions[col][row]
        if isinstance(piece, Stone) and piece.color == color and piece.marked == False:
            self.positions[col][row].marked = True
            group.append([col, row])

            if row - 1 >= 0:
                group, liberties = self.countLibertiesAndGroups(col, row-1, color, group, liberties) #oben
            if row + 1 < self.size:
                group, liberties = self.countLibertiesAndGroups(col, row+1, color, group, liberties) # unten
            if col - 1 >= 0:
                group, liberties = self.countLibertiesAndGroups(col-1, row, color, group, liberties) # links
            if col + 1 < self.size:
                group, liberties = self.countLibertiesAndGroups(col+1, row, color, group, liberties) # rechts
        elif not isinstance(piece, Stone) and not piece == 99:
            liberties += 1
        return group, liberties

    def displayStones(self):
        for col in range(self.size):
            for row in range(self.size):
                if isinstance(self.positions[col][row], Stone):
                    len = int(min(self.container.winfo_width(), self.container.winfo_height()))
                    length = int(len - 100)
                    self.boardPad = length / (self.container.board.size + 1)
                    self.positions[col][row].boardPad = self.boardPad
                    self.positions[col][row].draw(self.container.frame.canvas, "Game")

    def displayTerretories(self, anim=True):
        len = int(min(self.container.winfo_width(), self.container.winfo_height()))
        length = int(len - 100)
        self.boardPad = length / (self.container.board.size + 1)
        for col in range(self.size):
            for row in range(self.size):
                if anim:
                    time.sleep(0.02)
                if self.influence[col][row] != 0:
                    RoundRect(self.container.frame.canvas,
                        50 + self.boardPad + col * self.boardPad - self.boardPad / 2.5,
                        50 + self.boardPad + row * self.boardPad - self.boardPad / 2.5,
                        50 + self.boardPad + col * self.boardPad + self.boardPad / 2.5,
                        50 + self.boardPad + row * self.boardPad + self.boardPad / 2.5,
                        fill="gray20" if self.influence[col][row] > 0 else "gray80",
                        outline="gray20" if self.influence[col][row] > 0 else "gray80")
                    self.container.frame.canvas.update()
        self.displayStones()
        self.container.frame.canvas.update()
        if anim:
            time.sleep(3)

    def libertieForecast(self, col, row, colorToMove):
        positions = deepcopy(self.positions)
        self.positions[col][row] = Stone(col=col, row=row, color=colorToMove, boardPad=self.boardPad)
        group, liberties = self.countLibertiesAndGroups(col, row, colorToMove, [], 0)
        self.positions = positions
        return liberties

    def evalMove(self, move, colorToMove, liberties, bestMove, bestLiberties):
        if liberties <= bestLiberties and self.libertieForecast(move[0], move[1], colorToMove) >= 2:
            bestMove, bestLiberties = move, liberties
        return bestMove, bestLiberties

    def archiveBoard(self):
        self.history.append([deepcopy(self.positions), self.stonesCapturedByBlack, self.stonesCapturedByWhite])

    def undoMove(self):
        if len(self.history) == 1:
            return
        if self.container.gamemode == "ai":
            self.positions = deepcopy(self.history[-3][0])
            self.stonesCapturedByBlack, self.stonesCapturedByWhite = self.history[-3][1], self.history[-3][2]
            self.history.pop()
            self.history.pop()
            self.container.refresh()
            return
        self.positions = deepcopy(self.history[-2][0])
        self.stonesCapturedByBlack, self.stonesCapturedByWhite = self.history[-2][1], self.history[-2][2]
        self.history.pop()
        self.container.refresh()
        self.currentPlayer = "black" if self.currentPlayer == "white" else "white"

    def saveBoard(self):
        with open("assets/bin.dat", "wb") as f:
            try:
                pickle.dump([self.size, self.positions, self.currentPlayer, self.history], f)
                print("saved successfully")
            except: print("could not save")
            finally: f.close()
    def loadBoard(self):
        try:
            with open("assets/bin.dat", "rb") as f:
                loaded = pickle.load(f)
                board = Board(self.container, size=loaded[0])
                board.positions = loaded[1]
                board.currentPlayer = loaded[2]
                board.history = loaded[3]
                print("loaded sucessfully")
        except:
            board = Board(self.container, 9)
            print("loading failed")
        finally: f.close()
        return board

