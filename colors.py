colors = {
    "RED": [0, "#E88878"],
    "ORANGE": [1, "#E8AB5A"],
    "VIOLET": [2, "#8C8DEA"],
    "GREEN": [3, "#7CD072"],
    "CYAN": [4, "#53CCC5"],
    "BLUE": [5, "#5DADEA"],
    "PINK": [6, "#E87499"],
    "RED_DARK_RED": [7, "#993037"],
    "ORANGE_DARK_ORANGE": [8, "#C35814"],
    "VIOLET_DARK_VIOLET": [9, "#5E31C8"],
    "GREEN_DARK_GREEN": [10, "#177E2D"],
    "CYAN_DARK_CYAN": [11, "#045D7F"],
    "BLUE_DARK_BLUE": [12, "#0A5493"],
    "PINK_DARK_PINK": [13, "#8E376E"],
    "BLUE_WHITE_RED": [14, "#5DADEA"],
    "ORANGE_WHITE_GREEN": [15, "#E8AB5A"],
    "GREEN_WHITE_RED": [16, "#7CD072"],
    "CYAN_WHITE_GREEN": [17, "#53CCC5"],
    "CYAN_YELLOW_PINK": [18, "#53CCC5"],
    "VIOLET_YELLOW_ORANGE": [19, "#8C8DEA"],
    "BLUE_WHITE_ORANGE": [20, "#5DADEA"],
    "DYNAMIC": [21, "#8C8DEA"]
}


def get_color(s: str):
    for color in colors:
        if color in s:
            return colors[color][1]