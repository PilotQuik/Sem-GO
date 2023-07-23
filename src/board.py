

class Board:
    def __init__(self, container, size=9):
        self.container = container
        self.size = size
        self.positions = [[0 for row in range(self.size)] for col in range(self.size)]

    def saveBoard(self):
        pass

