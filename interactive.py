import pygame
import random
from blast import KnifeBlast
from enums import Direction
from settings import KROK
from interface import ManageInterface


def move(keys, player):
    if keys[pygame.K_UP]:
        if keys[pygame.K_LEFT]:
            player.update(-KROK, -KROK, Direction.GORALEWO)
        elif keys[pygame.K_RIGHT]:
            player.update(KROK, -KROK, Direction.GORAPRAWO)
        else:
            player.update(0, -KROK, Direction.GORA)
    elif keys[pygame.K_DOWN]:
        if keys[pygame.K_LEFT]:
            player.update(-KROK, KROK, Direction.DOLLEWO)
        elif keys[pygame.K_RIGHT]:
            player.update(KROK, KROK, Direction.DOLPRAWO)
        else:
            player.update(0, KROK, Direction.DOL)
    elif keys[pygame.K_LEFT]:
        player.update(-KROK, 0, Direction.LEWO)
    elif keys[pygame.K_RIGHT]:
        player.update(KROK, 0, Direction.PRAWO)
    elif keys[pygame.K_d]:
        player.hp -= 10


def moveenemy(enemy, player, sprites):
    krok = KROK/2
    oldx = enemy.rect.x
    oldy = enemy.rect.y
    oldd = enemy.direction

    x = player.rect.x - enemy.rect.x
    y = player.rect.y - enemy.rect.y
    eps = 10

    if abs(abs(x)-abs(y)) < eps:
        if x > 0:
            if y < 0:
                enemy.update(krok, -krok, Direction.GORAPRAWO)
            elif y > 0:
                enemy.update(krok, krok, Direction.DOLPRAWO)
            else:
                enemy.update(krok, 0, Direction.PRAWO)
        elif x < 0:
            if y < 0:
                enemy.update(-krok, -krok, Direction.GORALEWO)
            elif y > 0:
                enemy.update(-krok, krok, Direction.DOLLEWO)
            else:
                enemy.update(-krok, 0, Direction.LEWO)
        else:  # x == 0
            if y < 0:
                enemy.update(0, -krok, Direction.GORA)
            elif y > 0:
                enemy.update(0, krok, Direction.DOL)
    elif abs(x) > abs(y):
        if x > 0:
            enemy.update(krok, 0, Direction.PRAWO)
        elif x < 0:
            enemy.update(-krok, 0, Direction.LEWO)
    else:
        if y < 0:
            enemy.update(0, -krok, Direction.GORA)
        elif y > 0:
            enemy.update(0, krok, Direction.DOL)

    if len(pygame.sprite.spritecollide(enemy, sprites, False)) > 1:
        enemy.set_position(oldx, oldy, oldd)
        #movecorrection(enemy, sprites)


def movecorrection(enemy, sprites):
    rd = random.choice(list(Direction))
    krok = KROK//2
    oldx = enemy.rect.x
    oldy = enemy.rect.y
    oldd = enemy.direction

    if rd == Direction.GORAPRAWO:
        enemy.update(krok, -krok, Direction.GORAPRAWO)
    elif rd == Direction.DOLPRAWO:
        enemy.update(krok, krok, Direction.DOLPRAWO)
    elif rd == Direction.PRAWO:
        enemy.update(krok, 0, Direction.PRAWO)
    elif rd == Direction.GORALEWO:
        enemy.update(-krok, -krok, Direction.GORALEWO)
    elif rd == Direction.DOLLEWO:
        enemy.update(-krok, krok, Direction.DOLLEWO)
    elif rd == Direction.LEWO:
        enemy.update(-krok, 0, Direction.LEWO)
    elif rd == Direction.GORA:
        enemy.update(0, -krok, Direction.GORA)
    elif rd == Direction.DOL:
        enemy.update(0, krok, Direction.DOL)

    if len(pygame.sprite.spritecollide(enemy, sprites, False)) > 1:
        enemy.set_position(oldx, oldy, oldd)


def attack(keys, player, sprites, inter):
    if not keys[pygame.K_SPACE] or pygame.time.get_ticks() - inter.last_attack < 500:
        return
    sprites.add(player.selectedgun.blast(player, player.direction))
    inter.last_attack = pygame.time.get_ticks()


def changeweapon(keys, inter: ManageInterface, player):
    what = None
    if keys[pygame.K_1]:
        what = 0
    elif keys[pygame.K_2]:
        what = 1
    elif keys[pygame.K_3]:
        what = 2
    elif keys[pygame.K_4]:
        what = 3

    if what is not None:
        inter.select_square(what, player)
