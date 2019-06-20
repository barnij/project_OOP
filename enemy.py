import pygame
from characters import Character
from textures import img
from enums import Direction


class Enemy1(Character):
    def __init__(self, x, y):
        super().__init__()
        self.image = self.org_image = img.enemy1
        self.rect.x = x
        self.rect.y = y
        self.hp = 100
        self.selectedgun = None
