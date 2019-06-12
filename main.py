import pygame
from characters import Player
from settings import *
from moving import move
from textures import img

pygame.init()

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Gra")

Gracz = Player()

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(Gracz)

carryOn = True
clock = pygame.time.Clock()

while carryOn:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        carryOn = False
    move(keys, Gracz)


    # Drawing on Screen
    # screen.fill((0, 50, 0))
    screen.blit(img.background, (0, 0))

    all_sprites_list.draw(screen)

    # Refresh Screen
    pygame.display.flip()

    clock.tick(FRAMESPERSEC)

pygame.quit()
