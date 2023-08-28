from stone import Stone

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
                    self.positions[col][row].draw(self.container.frame.canvas)

    def calcValidMoves(self, activePlayer, *filter):
        if "liberties" in filter:
            libs = []
            # resetting groups and stone markers
            for col in range(self.size):
                for row in range(self.size):
                    pos = self.positions[col][row]
                    if not isinstance(pos, Stone):
                        if row - 1 >= 0:
                            posNord = self.positions[col][row - 1]
                            if isinstance(posNord, Stone):
                                if not posNord.color == activePlayer:
                                    libs.append([col, row])
                        if row + 1 < self.size:
                            posSüd = self.positions[col][row + 1]
                            if isinstance(posSüd, Stone):
                                if not posSüd.color == activePlayer:
                                    libs.append([col, row])
                        if col - 1 >= 0:
                            posWest = self.positions[col - 1][row]
                            if isinstance(posWest, Stone):
                                 if not posWest.color == activePlayer:
                                    libs.append([col, row])
                        if col + 1 < self.size:
                            posOst = self.positions[col + 1][row]
                            if isinstance(posOst, Stone):
                                if not posOst.color == activePlayer:
                                    libs.append([col, row])
            return libs

    def processStones(self, color):
        # resetting groups and stone markers and removing 99 markers
        self.group = []
        for col in range(self.size):
            for row in range(self.size):
                pos = self.positions[col][row]
                if isinstance(pos, Stone) and pos.marked == True:
                    pos.marked = False
                elif pos == 99:
                    self.positions[col][row] = 0
        # calc groups and delete groups of opposite color
        for col in range(self.size):
            for row in range(self.size):
                pos = self.positions[col][row]
                if isinstance(pos, Stone) and not pos.marked and pos.color != color:
                    # --------------------------------count
                    group, liberties = self.countLibertiesAndGroups(col, row, color, group=[], liberties=0)

                    if liberties == 0:
                        for pos in group:
                            #print("-- deleted")
                            self.positions[pos[0]][pos[1]] = 99
                            self.container.refresh()
                    else: self.group.append(group)
        # calc groups and delete groups of rest
        for col in range(self.size):
            for row in range(self.size):
                pos = self.positions[col][row]
                if isinstance(pos, Stone) and not pos.marked:
                    # --------------------------------count
                    group, liberties = self.countLibertiesAndGroups(col, row, self.positions[col][row].color, group=[], liberties=0)

                    if liberties == 0:
                        for pos in group:
                            #print("-- deleted")
                            self.positions[pos[0]][pos[1]] = 99
                            self.container.refresh()
                    else: self.group.append(group)
        #print("<>", self.group)

    def checkPattern(self):
        pass

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
        pass

