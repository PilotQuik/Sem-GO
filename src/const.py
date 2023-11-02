MENU_WIDTH = 852
MENU_HEIGHT = 480

OPT_WIDTH = 600
OPT_HEIGHT = 530

GAME_WIDTH = 900
GAME_HEIGHT = 900

ROWS = 19
COLS = 19
SQSIZE = GAME_WIDTH // COLS

FONT = ""
TRANSPARENT = "#fefefe"
# classic theme
BACKGROUND = "#c8b599"
BUTTON_COL = "#000000"
BUTTON_COL_CLICKED = "#ffa200"
BUTTON_COL_SELECTED = "#005eff"
BOARD_COL = "#c8b599"
BOARD_LINE = "#000000"
HOVER_B = "gray20"
HOVER_W = "gray80"
#light theme
BACKGROUND_LIGHT = "#FFFFFF"
BUTTON_COL_LIGHT = "#000000"
BUTTON_COL_CLICKED_LIGHT = "#ffa200"
BUTTON_COL_SELECTED_LIGHT = "#005eff"
BOARD_COL_LIGHT = "#FFFFFF"
BOARD_LINE_LIGHT = "#000000"
HOVER_B_LIGHT = "gray20"
HOVER_W_LIGHT = "gray80"
#dark theme
BACKGROUND_DARK = "#232931"
BUTTON_COL_DARK = "#FFE0B8"
BUTTON_COL_CLICKED_DARK = "#ffa200"
BUTTON_COL_SELECTED_DARK = "#005eff"
BOARD_COL_DARK = "#232931"
BOARD_LINE_DARK = "#FFE0B8"
HOVER_B_DARK = "gray20"
HOVER_W_DARK = "gray80"


PATTERNS = [  # rule: [[own color], [other color]], [0, 0] = place location
    [[[-1, 0], [1, 0]], [0, 1]],  # a standard ------
    [[[0, -1], [0, 1]], [-1, 0]],
    [[[-1, 0], [1, 0]], [0, -1]],
    [[[0, -1], [0, 1]], [1, 0]],

    [[[-1, 0], [1, 1]], [0, 1]],  # b standard ------
    [[[0, -1], [-1, 1]], [-1, 0]],
    [[[-1, -1], [1, 0]], [0, -1]],
    [[[1, -1], [0, 1]], [0, 1]],

    [[[-1, 1], [1, 0]], [0, 1]],  # b flip
    [[[-1, -1], [0, 1]], [-1, 0]],
    [[[-1, 0], [1, -1]], [0, -1]],
    [[[0, -1], [1, 1]], [1, 0]],

    [[[-1, -1], [1, -1]], [0, -1]],  # c standard ------
    [[[1, -1], [1, 1]], [1, 0]],
    [[[-1, 1], [1, 1]], [0, 1]],
    [[[-1, -1], [-1, 1]], [-1, 0]],

    [[[-1, 0], [2, 0]], [0, 1]],  # d standard ------
    [[[0, -1], [0, 2]], [-1, 0]],
    [[[-2, 0], [1, 0]], [0, -1]],
    [[[0, -2], [0, 1]], [1, 0]],

    [[[-2, 0], [1, 0]], [0, 1]],  # d flip
    [[[0, -2], [0, 1]], [-1, 0]],
    [[[-1, 0], [2, 0]], [0, -1]],
    [[[0, -1], [0, 2]], [1, 0]],

    [[[-2, 0], [2, 0]], [0, 1]],  # e standard ------
    [[[0, -2], [0, 2]], [-1, 0]],
    [[[-2, 0], [2, 0]], [0, -1]],
    [[[0, -2], [0, 2]], [1, 0]],

    [[[-2, 0], [-1, -1]], [0, -1]],  # f standard ------
    [[[0, -2], [1, -1]], [1, 0]],
    [[[2, 0], [1, 1]], [0, 1]],
    [[[0, 2], [-1, 1]], [-1, 0]],

    [[[1, -1], [2, 0]], [0, -1]],  # f flip
    [[[1, 1], [0, 2]], [1, 0]],
    [[[-2, 0], [-1, 1]], [0, 1]],
    [[[0, -2], [-1, -1]], [-1, 0]],

    [[[-1, -1], [1, -1]], [1, 0]],  # g standard ------
    [[[1, -1], [1, 1]], [0, 1]],
    [[[--1, 1], [1, 1]], [-1, 0]],
    [[[-1, -1], [-1, 1]], [0, -1]],

    [[[-1, -1], [1, -1]], [-1, 0]],  # g flip
    [[[1, -1], [1, 1]], [0, -1]],
    [[[-1, 1], [1, 1]], [1, 0]],
    [[[-1, -1], [-1, 1]], [0, 1]],

]

PATTERNS2 = [

    #[[col1], [col2], [col1-pos], weight]

]