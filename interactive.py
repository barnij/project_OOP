import pygame
from enums import Direction
from settings import KROK
from interface import ManageInterface


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


def changeweapon(keys, inter: ManageInterface, player):
    what = None
    if keys[pygame.K_1]:
        what = 0
    elif keys[pygame.K_2]:
        what = 1
    elif keys[pygame.K_3]:
        what = 2
    elif keys[pygame.K_4]:
        what = 3

    if what is not None:
        inter.select_square(what)
        player.selectedgun = inter.squares[what].gun
