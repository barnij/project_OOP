import pygame
from enum import Enum
from settings import KROK


class Direction(Enum):
    LEWO = 0
    PRAWO = 1
    GORA = 2
    DOL = 3
    GORALEWO = 4
    GORAPRAWO = 5
    DOLLEWO = 6
    DOLPRAWO = 7


def move(keys, player):
    if keys[pygame.K_UP]:
        if keys[pygame.K_LEFT]:
            player.update(-KROK, -KROK, Direction.GORALEWO)
        elif keys[pygame.K_RIGHT]:
            player.update(KROK, -KROK, Direction.GORAPRAWO)
        else:
            player.update(0, -KROK, Direction.GORA)
    elif keys[pygame.K_DOWN]:
        if keys[pygame.K_LEFT]:
            player.update(-KROK, KROK, Direction.DOLLEWO)
        elif keys[pygame.K_RIGHT]:
            player.update(KROK, KROK, Direction.DOLPRAWO)
        else:
            player.update(0, KROK, Direction.DOL)
    elif keys[pygame.K_LEFT]:
        player.update(-KROK, 0, Direction.LEWO)
    elif keys[pygame.K_RIGHT]:
        player.update(KROK, 0, Direction.PRAWO)
