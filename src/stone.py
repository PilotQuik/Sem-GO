

class Stone:
    def __init__(self, col, row, color, boardPad, marked=False):
        self.col = col
        self.row = row
        self.color = color
        self.marked = marked
        self.boardPad = boardPad

    def draw(self, canvas):
        canvas.create_oval(
            50 + self.boardPad + self.col * self.boardPad - self.boardPad / 2.5,
            50 + self.boardPad + self.row * self.boardPad - self.boardPad / 2.5,
            50 + self.boardPad + self.col * self.boardPad + self.boardPad / 2.5,
            50 + self.boardPad + self.row * self.boardPad + self.boardPad / 2.5,
            fill="black" if self.color == "black" else "white")