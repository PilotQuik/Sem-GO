import pickle

from stone import Stone
from const import *

class Board:
    def __init__(self, container, size=9):
        self.container = container
        self.size = size
        self.positions = [[0 for row in range(self.size)] for col in range(self.size)]
        self.validMoves = []
        self.currentPlayer = "black"

    def displayStones(self):
        for col in range(self.size):
            for row in range(self.size):
                if isinstance(self.positions[col][row], Stone):
                    len = int(min(self.container.winfo_width(), self.container.winfo_height()))
                    length = int(len - 100)
                    boardPad = length / (self.container.board.size + 1)
                    self.positions[col][row].boardPad = boardPad
                    self.positions[col][row].draw(self.container.frame.canvas, "Game")

    def calcValidMoves(self, activePlayer, *filter):
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
                        if not neighbours == 4 and isLib: libs.append([col, row]); print("added ", col, row)
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
        if "self" in filter:
            col, row = filter[1][0], filter[1][1]
            pos = self.positions[col][row]
            neighbours = 0
            isValid = False
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
                if not neighbours == 4: isValid = True; print("added ", col, row)
            return isValid


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
            cheeckGroup, checkLiberties = self.countLibertiesAndGroups(checkMove[0], checkMove[1], pos.color, group=[], liberties=0)
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
        # DELETE -------------------------------------------------------------------------------------------------------
        if checkMove == None:
            for pos in stonesToDeleteB if color == "white" else stonesToDeleteW:
                self.positions[pos[0]][pos[1]] = 99
                self.container.refresh()
        else:
            toDelete = stonesToDeleteB if color == "white" else stonesToDeleteW
            if checkLiberties == 0 and toDelete == []:
                return False # not valid
            else: return True # valid

    def checkPattern(self, color):
        matches = []
        for col in range(self.size):
            for row in range(self.size):
                for pattern in PATTERNS: # cycle patterns
                    match = 0
                    for ownColor in pattern[0]:
                        if (col + ownColor[0] in range(0, self.size) and row + ownColor[1] in range(0, self.size)
                                and isinstance(self.positions[col + ownColor[0]][row + ownColor[1]], Stone)):
                            if self.positions[col + ownColor[0]][row + ownColor[1]].color == color:
                                match += 1
                    if (col + pattern[1][0] in range(0, self.size) and row + pattern[1][1] in range(0, self.size)
                            and isinstance(self.positions[col + pattern[1][0]][row + pattern[1][1]], Stone)):
                        if self.positions[col + pattern[1][0]][row + pattern[1][1]].color != color:
                            match +=1
                    if match == 3 and not [col, row] in matches and self.positions[col][row] == 0:
                        matches.append([col, row])
        return matches

    def getGroups(self):
        # [color, liberties, [positions]]
        groups = []
        # RESET --------------------------------------------------------------------------------------------------------
        for col in range(self.size):
            for row in range(self.size):
                pos = self.positions[col][row]
                if isinstance(pos, Stone) and pos.marked == True:
                    pos.marked = False
                elif pos == 99:
                    self.positions[col][row] = 0
        # PROCESS ------------------------------------------------------------------------------------------------------
        for col in range(self.size):
            for row in range(self.size):
                pos = self.positions[col][row]
                if isinstance(pos, Stone) and not pos.marked:
                    # --------------------------------count
                    group, liberties = self.countLibertiesAndGroups(col, row, pos.color, group=[], liberties=0)
                    groups.append([pos.color, liberties, group])
        return groups

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


    def saveBoard(self):
        with open("assets/bin.dat", "wb") as f:
            try:
                pickle.dump([self.size, self.positions, self.currentPlayer], f)
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
                print("loaded sucessfully")
        except:
            board = Board(self.container, 9)
            print("loading failed")
        finally: f.close()
        return board

