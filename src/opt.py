from tkinter import ttk
from tkinter import *
from const import *
from custom import *
from game import Game


class Opt(ttk.Frame):
    def __init__(self, container, width=OPT_WIDTH, height=OPT_HEIGHT):
        super().__init__(container)

        self.container = container
        self.width = width
        self.height = height

        self.container.title("Options")
        self.container.resizable(False, False)
        self.container.minsize(OPT_WIDTH, OPT_HEIGHT)

        centerPos = self.container.findCenter(winHeight=self.height, winWidth=self.width)
        self.container.geometry(f"{self.width}x{self.height}+{centerPos[0]}+{centerPos[1]}")

        self.displayCanvas()

    def displayCanvas(self):
        self.canvas = Canvas(self, width=self.width, height=self.height, bg='white')
        self.canvas.pack(side=TOP, fill=BOTH, expand=NO)

        # gamemode selector
        self.ai_label = Label(self.canvas, text="GAMEMODE", background=BACKGROUND, font=(FONT, 15, "bold"))
        self.ai_label.place(x=5, y=5)
        self.vs_ai = Button_(20, 60, self.canvas, name="vs-player-button", text="VS PLAYER", font=(FONT, 25, "bold"))
        RoundRect(self.canvas, 10, 40, 290, 110, fill="White", outline=BUTTON_COL, width=3)
        self.vs_player = Button_(405, 55, self.canvas, name="vs-ai-button", text="VS AI",font=(FONT, 25, "bold"))
        RoundRect(self.canvas, 310, 40, 590, 110, fill="White", outline=BUTTON_COL, width=3)
        # ai level selector
        self.ai_label = Label(self.canvas, text="AI DIFFICULTY", background=BACKGROUND, font=(FONT, 15, "bold"))
        self.ai_label.place(x=5, y=115)
        RoundRect(self.canvas, 10, 150, 193, 220, fill="White", outline=BUTTON_COL, width=3)
        RoundRect(self.canvas, 203, 150, 397, 220, fill="White", outline=BUTTON_COL, width=3)
        RoundRect(self.canvas, 407, 150, 590, 220, fill="White", outline=BUTTON_COL, width=3)
        # board selector
        self.ai_label = Label(self.canvas, text="BOARD SIZE", background=BACKGROUND, font=(FONT, 15, "bold"))
        self.ai_label.place(x=5, y=225)
        RoundRect(self.canvas, 10, 260, 193, 340, fill="White", outline=BUTTON_COL, width=3)
        RoundRect(self.canvas, 203, 260, 397, 340, fill="White", outline=BUTTON_COL, width=3)
        RoundRect(self.canvas, 407, 260, 590, 340, fill="White", outline=BUTTON_COL, width=3)

        Button_(10, self.height - 65, self.canvas, name="back-button", text="<",
                                   font=(FONT, 40, "bold"))
        Button_(230, self.height - 65, self.canvas, name="play-button", text="PLAY",
                                   font=(FONT, 40, "bold"))

        self.pack()