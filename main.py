import pygame
from blast import KnifeBlast
from player import Player
from interface import ManageInterface
from interactive import move, moveenemy, changeweapon, attack
from settings import *
from weapons import Knife, Pistol, Mp40
from enemy import Enemy1

pygame.init()

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Gra")

gracz = Player()
enemy1 = Enemy1(200, 100)
enemy2 = Enemy1(100, 200)
inter = ManageInterface(gracz)
knife = Knife(0, 0)
pistol = Pistol(0, 0)
mp40 = Mp40(0, 0)
inter.add_gun(knife, 0)
inter.make_active_square(0)
inter.add_gun(pistol, 1)
inter.make_active_square(1)
inter.add_gun(mp40, 3)
inter.make_active_square(3)
inter.select_square(0, gracz )

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(gracz)
all_sprites_list.add(enemy1)
all_sprites_list.add(enemy2)

all_blasts = pygame.sprite.Group()

all_enemys = pygame.sprite.Group()
all_enemys.add(enemy1, enemy2)

carryOn = True
clock = pygame.time.Clock()

while carryOn:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        carryOn = False
    move(keys, gracz)
    attack(keys, gracz, all_blasts, inter)
    moveenemy(enemy1, gracz, all_sprites_list)
    moveenemy(enemy2, gracz, all_sprites_list)
    changeweapon(keys, inter, gracz)

    all_blasts.update()

    # Drawing on Screen
    inter.draw(screen, gracz)
    all_sprites_list.draw(screen)
    all_blasts.draw(screen)

    # Refresh Screen
    pygame.display.flip()

    clock.tick(FRAMESPERSEC)

pygame.quit()
