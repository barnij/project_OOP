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