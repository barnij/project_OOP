import pygame


class Textures:
    def __init__(self):
        self.background = pygame.image.load('images/background.png')
        self.player = pygame.image.load('images/player.png')
        self.chooseweapon = pygame.image.load('images/chooseweapon.png')
        self.numbersofweapons = pygame.image.load('images/numbersofweapons.png')
        self.knife = pygame.image.load('images/knife_gun1.png')
        self.knife_mini = pygame.image.load('images/gun1_mini.png')
        self.knife_square = pygame.image.load('images/gun1_square.png')
        self.pistol = pygame.image.load('images/pistol_gun2.png')
        self.pistol_mini = pygame.image.load('images/gun2_mini.png')
        self.pistol_square = pygame.image.load('images/gun2_square.png')
        self.mp40 = pygame.image.load('images/mp40_gun4.png')
        self.mp40_mini = pygame.image.load('images/gun4_mini.png')
        self.mp40_square = pygame.image.load('images/gun4_square.png')
        self.tompson = pygame.image.load('images/tompson_gun3.png')
        self.tompson_mini = pygame.image.load('images/gun3_mini.png')
        self.tompson_square = pygame.image.load('images/gun3_square.png')
        self.enemy1 = pygame.image.load('images/enemy1.png')
        self.enemy2 = pygame.image.load('images/enemy2.png')
        self.enemy3 = pygame.image.load('images/enemy3.png')
        self.gameover = pygame.image.load('images/gameover.png')
        self.healthbar = pygame.image.load('images/healthbar.png')
        self.win = pygame.image.load('images/win.png')


img = Textures()
