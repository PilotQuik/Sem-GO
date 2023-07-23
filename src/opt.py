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

        self.canvas = Canvas(self, width=self.width, height=self.height, bg='white')
        self.canvas.pack(side=TOP, fill=BOTH, expand=NO)
        self.displayCanvas()

    def displayCanvas(self):

        # gamemode selector
        self.ai_label = Label(self.canvas, text="GAMEMODE", background=BACKGROUND, font=(FONT, 15, "bold"))
        self.ai_label.place(x=5, y=5)
        self.vs_ai = Button_(50, 55, self.canvas, name="vs-player-button", text="VS PLAYER", font=(FONT, 25, "bold"))
        RoundRect(self.canvas, 10, 40, 290, 110, fill="White", width=3,
                  outline=BUTTON_COL_SELECTED if self.container.gamemode == "player" else BUTTON_COL)
        self.vs_player = Button_(405, 55, self.canvas, name="vs-ai-button", text="VS AI",font=(FONT, 25, "bold"))
        RoundRect(self.canvas, 310, 40, 590, 110, fill="White", width=3,
                  outline=BUTTON_COL_SELECTED if self.container.gamemode == "ai" else BUTTON_COL)
        # ai level selector
        self.ai_label = Label(self.canvas, text="AI DIFFICULTY", background=BACKGROUND, font=(FONT, 15, "bold"))
        self.ai_label.place(x=5, y=115)
        self.easy_ai = Button_(53, 165, self.canvas, name="easy-ai-button", text="EASY", font=(FONT, 25, "bold"))
        RoundRect(self.canvas, 10, 150, 193, 220, fill="White", width=3,
                  outline=BUTTON_COL_SELECTED if self.container.ai_level == "easy" else BUTTON_COL)
        self.medium_ai = Button_(230, 165, self.canvas, name="medium-ai-button", text="MEDIUM", font=(FONT, 25, "bold"))
        RoundRect(self.canvas, 203, 150, 397, 220, fill="White", width=3,
                  outline=BUTTON_COL_SELECTED if self.container.ai_level == "medium" else BUTTON_COL)
        self.hard_ai = Button_(450, 165, self.canvas, name="hard-ai-button", text="HARD", font=(FONT, 25, "bold"))
        RoundRect(self.canvas, 407, 150, 590, 220, fill="White", width=3,
                  outline=BUTTON_COL_SELECTED if self.container.ai_level == "hard" else BUTTON_COL)
        # board selector
        self.ai_label = Label(self.canvas, text="BOARD SIZE", background=BACKGROUND, font=(FONT, 15, "bold"))
        self.ai_label.place(x=5, y=225)
        self.x9 = Button_(65, 275, self.canvas, name="9x9-button", text="9 : 9", font=(FONT, 25, "bold"))
        RoundRect(self.canvas, 10, 260, 193, 330, fill="White", width=3,
                  outline=BUTTON_COL_SELECTED if self.container.board_size == 9 else BUTTON_COL)
        self.x13 = Button_(245, 275, self.canvas, name="13x13-button", text="13 : 13", font=(FONT, 25, "bold"))
        RoundRect(self.canvas, 203, 260, 397, 330, fill="White", width=3,
                  outline=BUTTON_COL_SELECTED if self.container.board_size == 13 else BUTTON_COL)
        self.x19 = Button_(445, 275, self.canvas, name="19x19-button", text="19 : 19", font=(FONT, 25, "bold"))
        RoundRect(self.canvas, 407, 260, 590, 330, fill="White", width=3,
                  outline=BUTTON_COL_SELECTED if self.container.board_size == 19 else BUTTON_COL)

        Button_(10, self.height - 65, self.canvas, name="back-button", text="<",
                                   font=(FONT, 40, "bold"))
        Button_(230, self.height - 65, self.canvas, name="play-button", text="PLAY",
                                   font=(FONT, 40, "bold"))

        self.pack()