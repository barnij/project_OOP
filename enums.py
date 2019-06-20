from enum import Enum


class Direction(Enum):
    LEWO = 0
    PRAWO = 1
    GORA = 2
    DOL = 3
    GORALEWO = 4
    GORAPRAWO = 5
    DOLLEWO = 6
    DOLPRAWO = 7


class Squares(Enum):
    FIRST = (3, 604)
    SECOND = (103, 604)
    THIRD = (203, 604)
    FOURTH = (303, 604)


class Color(Enum):
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    SILVER = (192, 192, 192)
    GRAY = (128, 128, 128)
    PURPLE = (128, 0, 128)
    ORANGE = (255, 165, 0)
