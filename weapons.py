import pygame


class Weapon(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.rect = pygame.Rect((x, y), [20, 20])
        self.image = None
