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

        self.canvas = Canvas(self, width=self.width, height=self.height, bg=BACKGROUND)
        self.canvas.pack(side=TOP, fill=BOTH, expand=NO)
        self.displayCanvas()

    def displayCanvas(self):
        bg = self.container.background
        button_col = self.container.button_col
        button_col_selected = self.container.button_col_selected
        self.canvas.destroy()
        self.canvas = Canvas(self, width=self.width, height=self.height, bg=bg)
        self.canvas.pack(side=TOP, fill=BOTH, expand=NO)
        # gamemode selector
        self.gamemode_label = Label(self.canvas, text="GAMEMODE", background=bg, font=(FONT, 15, "bold"),
                                    bg=bg, fg=button_col)
        self.gamemode_label.place(x=5, y=5)
        self.vs_ai = Button_(50, 55, self.canvas, name="vs-player-button", text="VS PLAYER", font=(FONT, 25,
                                                                    "bold"), bg=bg, fg=button_col)
        RoundRect(self.canvas, 10, 40, 290, 110, fill=bg, width=3,
                  outline=button_col_selected if self.container.gamemode == "player" else button_col)
        self.vs_player = Button_(405, 55, self.canvas, name="vs-ai-button", text="VS AI", font=(FONT, 25, "bold"),
                                 bg=bg, fg=button_col)
        RoundRect(self.canvas, 310, 40, 590, 110, fill=bg, width=3,
                  outline=button_col_selected if self.container.gamemode == "ai" else button_col)
        # ai level selector
        self.ai_label = Label(self.canvas, text="AI DIFFICULTY", background=bg, font=(FONT, 15, "bold"),
                              bg=bg, fg=button_col)
        self.ai_label.place(x=5, y=115)
        self.easy_ai = Button_(53, 165, self.canvas, name="easy-ai-button", text="EASY", font=(FONT, 25, "bold"),
                               bg=bg, fg=button_col)
        RoundRect(self.canvas, 10, 150, 193, 220, fill=bg, width=3,
                  outline=button_col_selected if self.container.ai_level == "easy" else button_col)
        self.medium_ai = Button_(230, 165, self.canvas, name="medium-ai-button", text="MEDIUM", font=(FONT, 25,
                                                                    "bold"), bg=bg, fg=button_col)
        RoundRect(self.canvas, 203, 150, 397, 220, fill=bg, width=3,
                  outline=button_col_selected if self.container.ai_level == "medium" else button_col)
        self.hard_ai = Button_(450, 165, self.canvas, name="hard-ai-button", text="HARD", font=(FONT, 25, "bold"),
                               bg=bg, fg=button_col)
        RoundRect(self.canvas, 407, 150, 590, 220, fill=bg, width=3,
                  outline=button_col_selected if self.container.ai_level == "hard" else button_col)
        # board selector
        self.board_label = Label(self.canvas, text="BOARD SIZE", background=bg, font=(FONT, 15, "bold"),
                                 bg=bg, fg=button_col)
        self.board_label.place(x=5, y=225)
        self.x9 = Button_(65, 275, self.canvas, name="9x9-button", text="9 : 9", font=(FONT, 25, "bold"),
                          bg=bg, fg=button_col)
        RoundRect(self.canvas, 10, 260, 193, 330, fill=bg, width=3,
                  outline=button_col_selected if self.container.board.size == 9 else button_col)
        self.x13 = Button_(245, 275, self.canvas, name="13x13-button", text="13 : 13", font=(FONT, 25, "bold"),
                           bg=bg, fg=button_col)
        RoundRect(self.canvas, 203, 260, 397, 330, fill=bg, width=3,
                  outline=button_col_selected if self.container.board.size == 13 else button_col)
        self.x19 = Button_(445, 275, self.canvas, name="19x19-button", text="19 : 19", font=(FONT, 25, "bold"),
                           bg=bg, fg=button_col)
        RoundRect(self.canvas, 407, 260, 590, 330, fill=bg, width=3,
                  outline=button_col_selected if self.container.board.size == 19 else button_col)
        # theme selector
        self.theme_label = Label(self.canvas, text="THEME", background=bg, font=(FONT, 15, "bold"),
                                 bg=bg, fg=button_col)
        self.theme_label.place(x=5, y=335)
        self.classic = Button_(27, 385, self.canvas, name="classic-button", text="CLASSIC", font=(FONT, 25,
                                                                    "bold"), bg=bg, fg=button_col)
        RoundRect(self.canvas, 10, 370, 193, 440, fill=bg, width=3,
                  outline=button_col_selected if self.container.theme == "classic" else button_col)
        self.light = Button_(248, 385, self.canvas, name="light-button", text="LIGHT", font=(FONT, 25, "bold"),
                             bg=bg, fg=button_col)
        RoundRect(self.canvas, 203, 370, 397, 440, fill=bg, width=3,
                  outline=button_col_selected if self.container.theme == "light" else button_col)
        self.dark = Button_(448, 385, self.canvas, name="dark-button", text="DARK", font=(FONT, 25, "bold"),
                            bg=bg, fg=button_col)
        RoundRect(self.canvas, 407, 370, 590, 440, fill=bg, width=3,
                  outline=button_col_selected if self.container.theme == "dark" else button_col)

        Button_(10, self.height - 70, self.canvas, name="back-button", text="<<",
                font=(FONT, 40, "bold"), bg=bg, fg=button_col)
        Button_(230, self.height - 70, self.canvas, name="play-button", text="PLAY",
                font=(FONT, 40, "bold"), bg=bg, fg=button_col)

        self.pack()