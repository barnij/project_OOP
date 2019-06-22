import pygame
from player import Player
from interface import ManageInterface
from interactive import move, moveenemies, changeweapon, attack, reacttoblast, attackenemy, spawnweapon, getweapon
from settings import *
from round import Round1

pygame.init()

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Projekt z przedmiotu \"Programowanie obiektowe\"")

gracz = Player()
inter = ManageInterface(gracz)

weapons = pygame.sprite.Group()

round = Round1(gracz)
inter.roundtext = round.text

carryOn = True
win = False
clock = pygame.time.Clock()

while carryOn:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        carryOn = False

    if round.ifnextround():
        round = round.next_round

        if round is None:
            win = True
            break
        else:
            inter.roundtext = round.text

    move(keys, gracz)
    attack(keys, gracz, round.blasts_group, inter)
    attackenemy(round.enemies_group, gracz, round.blasts_group)
    moveenemies(round.enemies_group, gracz, round.characters_group)
    if reacttoblast(round.blasts_group, round.characters_group, inter):
        break
    changeweapon(keys, inter, gracz)
    getweapon(weapons, gracz, inter)

    if pygame.time.get_ticks() - round.last_spawn_weapon > round.time_to_spawn_weapon:
        spawnweapon(weapons, round.available_weapons)
        round.last_spawn_weapon = pygame.time.get_ticks()

    round.blasts_group.update()

    # Drawing on Screen
    inter.draw(screen, gracz)
    weapons.draw(screen)
    for enemy in round.enemies_group:
        enemy.draw(screen)
    round.characters_group.draw(screen)
    round.blasts_group.draw(screen)


    # Refresh Screen
    pygame.display.flip()

    clock.tick(FRAMESPERSEC)

if carryOn:
    if win:
        inter.win(screen)
    else:
        inter.healthbar.draw(screen, True)
        inter.gameover(screen)
    pygame.display.flip()
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        if event.type == pygame.KEYDOWN:
            carryOn = False

pygame.quit()
