from stone import Stone

class Board:
    def __init__(self, container, size=9):
        self.container = container
        self.size = size
        self.positions = [[0 for row in range(self.size)] for col in range(self.size)]
        self.liberties = []

    def displayStones(self, row=None, col=None):
        self.group = []
        for i in range(self.size):
            for j in range(self.size):
                pos = self.positions[i][j]
                if isinstance(pos, Stone) and pos.marked == True:
                    pos.marked = False
        if row == None and col == None:
            for y in range(self.size):
                for x in range(self.size):
                    if isinstance(self.positions[x][y], Stone):
                        self.container.frame.canvas.create_oval(
                            self.container.frame.pad + self.container.frame.boardPad + x * self.container.frame.boardPad - self.container.frame.boardPad / 2.5,
                            self.container.frame.pad + self.container.frame.boardPad + y * self.container.frame.boardPad - self.container.frame.boardPad / 2.5,
                            self.container.frame.pad + self.container.frame.boardPad + x* self.container.frame.boardPad + self.container.frame.boardPad / 2.5,
                            self.container.frame.pad + self.container.frame.boardPad + y * self.container.frame.boardPad + self.container.frame.boardPad / 2.5,
                            fill="black" if self.positions[x][y].color == "black" else "white")

        elif isinstance(self.positions[col][row], Stone):
            self.container.frame.canvas.create_oval(
                self.container.frame.pad + self.container.frame.boardPad + col * self.container.frame.boardPad - self.container.frame.boardPad / 2.5,
                self.container.frame.pad + self.container.frame.boardPad + row * self.container.frame.boardPad - self.container.frame.boardPad / 2.5,
                self.container.frame.pad + self.container.frame.boardPad + col * self.container.frame.boardPad + self.container.frame.boardPad / 2.5,
                self.container.frame.pad + self.container.frame.boardPad + row * self.container.frame.boardPad + self.container.frame.boardPad / 2.5,
                fill="black" if self.positions[col][row].color == "black" else "white")

        for col in range(self.size):
            for row in range(self.size):
                if isinstance(self.positions[col][row], Stone) and self.positions[col][row].marked == False:
                    list = self.countLibertiesAndGroups(col, row, self.positions[col][row].color, [])
                    self.group.append(list)
        print(self.group)

    def countLibertiesAndGroups(self, col, row, color, list=[]):
        piece = self.positions[col][row]
        if isinstance(piece, Stone) and piece.color == color and piece.marked == False:

            self.positions[col][row].marked = True
            list.append((col, row))

            if not col - 1 < 0:
                list = self.countLibertiesAndGroups(col, row-1, color, list) #oben
            if not col + 1 > self.size:
                list = self.countLibertiesAndGroups(col, row+1, color, list) # unten
            if not row - 1 < 0:
                list = self.countLibertiesAndGroups(col-1, row, color, list) # links
            if not row + 1 > self.size:
                list = self.countLibertiesAndGroups(col+1, row, color, list) # rechts
        elif not isinstance(piece, Stone):
            self.positions[col][row] = 1
        return list


    def saveBoard(self):
        pass

