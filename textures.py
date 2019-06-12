import pygame


class Textures:
    def __init__(self):
        self.background = pygame.image.load('images/background.png')
        self.player = pygame.image.load('images/player.png')


img = Textures()