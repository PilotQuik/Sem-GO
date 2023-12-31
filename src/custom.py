from tkinter import *

from const import *

class Button_(Label):
    def __init__(self, x, y, container, name="!label", text="", fg=BUTTON_COL, font=("Impact", 10),
                 background=BACKGROUND, cursor="hand2", **kwargs):
        super().__init__(container)

        self.container = container
        self.x = x
        self.y = y
        self.name = name
        self.text = text
        self.fg = fg
        self.font = font
        self.background = background
        self.cursor = cursor

        self.button = Label(self.container, name=self.name, text=self.text, fg=self.fg, font=self.font,
                                 background=self.background, cursor=self.cursor, **kwargs)
        self.button.place(x=self.x, y=self.y)

class RoundRect:
    def __init__(self, container, x1, y1, x2, y2, radius=25, **kwargsPolygon):
        self.container = container

        self.points = [x1+radius, y1, x1+radius, y1, x2-radius, y1, x2-radius, y1, x2, y1, x2, y1+radius, x2, y1+radius,
              x2, y2-radius, x2, y2-radius, x2, y2, x2-radius, y2, x2-radius, y2, x1+radius, y2,  x1+radius, y2, x1, y2,
              x1, y2-radius, x1, y2-radius, x1, y1+radius, x1, y1+radius, x1, y1]

        self.roundRect = container.create_polygon(self.points, **kwargsPolygon, smooth=True)

class ProgressBar:
    def progressBar(length, progress, title):
        percentage = round(progress * 100, 2)
        bar = round(length * progress) * "-" + ">" + (length - round(length * progress)) * " "
        if progress != 1:
            print("\r", f"{title}: |{bar}| {percentage}%", end=" ")
        else:
            bar = (length + 1) * "-"
            print("\r", f"{title}: |{bar}| 100%", end="\n")

class Gif:
    def __init__(self, container, x, y, path, frameCnt, repeats):
        self.container = container
        self.repeats = repeats
        self.frameCnt = frameCnt
        self.frames = [PhotoImage(file=path + "/frame_%i.gif" % (i)) for i in range(self.frameCnt)]
        self.label = Label(self.container)
        self.label.place(x=x, y=y)
        self.i = 0

        self.container.after(0, self.update, 0)

    def update(self, ind):
        frame = self.frames[ind]
        ind += 1
        if ind == self.frameCnt:
            if self.i == self.repeats - 1:
                self.label.destroy()
                return
            ind = 0
            self.i += 1
        self.label.configure(image=frame)
        self.container.after(100, self.update, ind)