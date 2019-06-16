import pygame
from blast import KnifeBlast
from textures import img


class Weapon(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.rect = pygame.Rect((x, y), [20, 20])
        self.image = None
        self.mini = None
        self.blast = None


class Knife(Weapon):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.image = img.knife
        self.mini = img.knife_mini
        self.square = img.knife_square
        self.blast = KnifeBlast


class Pistol(Weapon):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.image = img.pistol
        self.mini = img.pistol_mini
        self.square = img.pistol_square


class Mp40(Weapon):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.image = img.mp40
        self.mini = img.mp40_mini
        self.square = img.mp40_square


class Tomposon(Weapon):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.image = img.tompson
        self.mini = img.tompson_mini
        self.square = img.tompson_square
