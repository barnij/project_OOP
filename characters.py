import pygame
from settings import ARENAWIDTH, ARENAHEIGHT, ARENAWIDTH_Q, ARENAHEIGHT_Q
from enums import Direction
from otherfunctions import rot_center
from textures import img


class Character(pygame.sprite.Sprite):
    """Główna klasa dla postaci"""

    def __init__(self):
        super().__init__()
        self.org_image = None
        self.image = None
        self.direction = Direction.GORA
        self.rect = pygame.Rect((0, 0), [40, 40])
        self.rect.x = ARENAWIDTH//2
        self.rect.y = ARENAHEIGHT//2
        self.hp = 100

    def update(self, x: int, y: int, d: Direction):
        self.rect.x += x
        self.rect.y += y
        self.direction = d

        if self.rect.x > ARENAWIDTH_Q:
            self.rect.x = ARENAWIDTH_Q
        elif self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y > ARENAHEIGHT_Q:
            self.rect.y = ARENAHEIGHT_Q
        elif self.rect.y < 0:
            self.rect.y = 0

        if d is Direction.LEWO:
            self.image = rot_center(self.org_image, 90)
        elif d is Direction.PRAWO:
            self.image = rot_center(self.org_image, -90)
        elif d is Direction.GORA:
            self.image = rot_center(self.org_image, 0)
        elif d is Direction.DOL:
            self.image = rot_center(self.org_image, 180)
        elif d is Direction.GORAPRAWO:
            self.image = rot_center(self.org_image, -45)
        elif d is Direction.GORALEWO:
            self.image = rot_center(self.org_image, 45)
        elif d is Direction.DOLLEWO:
            self.image = rot_center(self.org_image, 135)
        elif d is Direction.DOLPRAWO:
            self.image = rot_center(self.org_image, -135)
