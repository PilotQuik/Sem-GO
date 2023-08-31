MENU_WIDTH = 852
MENU_HEIGHT = 480

OPT_WIDTH = 600
OPT_HEIGHT = 530

GAME_WIDTH = 900
GAME_HEIGHT = 900

ROWS = 19
COLS = 19
SQSIZE = GAME_WIDTH // COLS

BACKGROUND = "white"
TRANSPARENT = "#fefefe"
BUTTON_COL = "black"
BUTTON_COL_CLICKED = "#ff9e17"
BUTTON_COL_SELECTED = "#1677ff"
HOVER_B = "gray20"
HOVER_W = "gray80"
FONT = ""

PATTERNS = [  # rule: [[own color], [other color]], [0, 0] = place location
    [[[-1, 0], [1, 0]], [0, 1]],  # a
    [[[-1, 0], [1, 1]], [0, 1]],  # b
    [[[-1, -1], [1, -1]], [0, -1]],  # c
    [[[-1, 0], [2, 0]], [0, 1]],  # d
    [[[-2, 0], [2, 0]], [0, 1]],  # e
    [[[-2, 0], [-1, -1]], [0, -1]],  # f
    [[[-1, -1], [1, -1]], [1, 0]],  # g
]
