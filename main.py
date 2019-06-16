import pygame
from blast import KnifeBlast
from player import Player
from interface import ManageInterface
from interactive import move, changeweapon
from settings import *
from weapons import Knife, Pistol, Mp40

pygame.init()

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Gra")

gracz = Player()
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
knife_blast = KnifeBlast(gracz, [20, 4])

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(gracz)

all_blasts = pygame.sprite.Group()
all_blasts.add(knife_blast)

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
    changeweapon(keys, inter, gracz)

    all_blasts.update()

    # Drawing on Screen
    inter.draw(screen, gracz)

    all_sprites_list.draw(screen)

    if pygame.sprite.collide_rect(knife_blast, gracz):
        pygame.draw.circle(screen, (100, 200, 200), [100, 100], 15)

    all_blasts.draw(screen)

    # Refresh Screen
    pygame.display.flip()

    clock.tick(FRAMESPERSEC)

pygame.quit()
