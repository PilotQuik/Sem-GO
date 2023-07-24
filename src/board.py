from stone import Stone

class Board:
    def __init__(self, container, size=9):
        self.container = container
        self.size = size
        self.positions = [[0 for row in range(self.size)] for col in range(self.size)]
        self.liberties = []
        self.blocks = []

    def displayStones(self):
        print(self)
        for col in range(self.size):
            for row in range(self.size):
                if isinstance(self.positions[col][row], Stone):
                    self.container.frame.canvas.create_oval(self.container.frame.pad + self.container.frame.boardPad + col * self.container.frame.boardPad - self.container.frame.boardPad / 2.5,
                          self.container.frame.pad + self.container.frame.boardPad + row * self.container.frame.boardPad - self.container.frame.boardPad / 2.5,
                          self.container.frame.pad + self.container.frame.boardPad + col * self.container.frame.boardPad + self.container.frame.boardPad / 2.5,
                          self.container.frame.pad + self.container.frame.boardPad + row * self.container.frame.boardPad + self.container.frame.boardPad / 2.5,
                          fill="black" if self.positions[col][row].color == "black" else "white")

    def calcLiberties(self):
        pass
    def saveBoard(self):
        pass

