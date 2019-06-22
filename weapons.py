import pygame
import random
from blast import KnifeBlast, PistolBlast, Mp40Blast, TompsonBlast
from textures import img
from enums import Direction
from otherfunctions import rot_center


class Weapon(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.rect = pygame.Rect((x, y), [20, 20])
        self.image = None
        self.mini = None
        self.blast = None
        self.plusammo = random.randrange(1, 16)

    def drawmini(self, player, screen):
        x = player.rect.x - 5
        y = player.rect.y - 5
        d = player.direction.value
        g = self.mini
        i = None

        if d is Direction.LEWO.value:
            i = rot_center(g, 90)
        elif d is Direction.PRAWO.value:
            i = rot_center(g, -90)
        elif d is Direction.GORA.value:
            i = rot_center(g, 0)
        elif d is Direction.DOL.value:
            i = rot_center(g, 180)
        elif d is Direction.GORAPRAWO.value:
            i = rot_center(g, -45)
        elif d is Direction.GORALEWO.value:
            i = rot_center(g, 45)
        elif d is Direction.DOLLEWO.value:
            i = rot_center(g, 135)
        elif d is Direction.DOLPRAWO.value:
            i = rot_center(g, -135)

        screen.blit(i, (x, y))


class Knife(Weapon):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.image = img.knife
        self.mini = img.knife_mini
        self.square = img.knife_square
        self.blast = KnifeBlast
        self.plusammo = 40


class Pistol(Weapon):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.image = img.pistol
        self.mini = img.pistol_mini
        self.square = img.pistol_square
        self.blast = PistolBlast


class Mp40(Weapon):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.image = img.mp40
        self.mini = img.mp40_mini
        self.square = img.mp40_square
        self.blast = Mp40Blast


class Tompson(Weapon):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.image = img.tompson
        self.mini = img.tompson_mini
        self.square = img.tompson_square
        self.blast = TompsonBlast
