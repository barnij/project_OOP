import pygame
import pygame.gfxdraw
from enums import Direction
from enums import Color
from settings import ARENAHEIGHT, CHAIN


class Blast(pygame.sprite.Sprite):
    def __init__(self, owner):
        super().__init__()
        self.image = None
        self.owner = owner
        self.enemy = owner.enemy
        self.time = None
        self.rect = None
        self.speed = 1
        self.vector = [0, 0]
        self.timetodestroy = 2000
        self.damage = 0

    def update(self):
        if self.time is not None:
            if pygame.time.get_ticks() - self.time >= self.timetodestroy:
                self.kill()

        if self.rect is not None:
            arenaheight_q = ARENAHEIGHT - CHAIN - self.image.get_height()

            if self.rect.y > arenaheight_q:
                self.kill()

            self.rect.x += self.vector[0]
            self.rect.y += self.vector[1]

    def correction(self, direction):
        """Poprawia vector i pozycję strzału w zależności
            od podanego kierunku
        """
        if direction == Direction.GORA:
            self.vector = [0, -self.speed]
            self.rect.x += 15
            self.rect.y -= 10
        elif direction == Direction.PRAWO:
            self.vector = [self.speed, 0]
            self.rect.y += 20
        elif direction == Direction.DOL:
            self.vector = [0, self.speed]
            self.rect.x -= 20
        elif direction == Direction.LEWO:
            self.vector = [-self.speed, 0]
            self.rect.y -= 20
        elif direction == Direction.GORALEWO:
            self.vector = [-self.speed, -self.speed]
            self.rect.x += 10
            self.rect.y -= 10
        elif direction == Direction.GORAPRAWO:
            self.vector = [self.speed, -self.speed]
            self.rect.x += 10
            self.rect.y += 10
        elif direction == Direction.DOLLEWO:
            self.vector = [-self.speed, self.speed]
            self.rect.x -= 10
            self.rect.y -= 10
        elif direction == Direction.DOLPRAWO:
            self.vector = [self.speed, self.speed]
            self.rect.x -= 10
            self.rect.y += 10

    def correctionimage(self, direction):
        if direction == Direction.PRAWO:
            self.image = pygame.transform.rotate(self.image, -90)
        elif direction == Direction.LEWO:
            self.image = pygame.transform.rotate(self.image, 90)
        elif direction == Direction.GORALEWO:
            self.image = pygame.transform.rotate(self.image, -45)
        elif direction == Direction.GORAPRAWO:
            self.image = pygame.transform.rotate(self.image, 45)
        elif direction == Direction.DOLLEWO:
            self.image = pygame.transform.rotate(self.image, -135)
        elif direction == Direction.DOLPRAWO:
            self.image = pygame.transform.rotate(self.image, 135)


class KnifeBlast(Blast):
    def __init__(self, owner, direction):
        super().__init__(owner)
        self.image = pygame.Surface([30, 30])
        self.image.set_alpha(50)
        self.image.fill(Color.SILVER.value)
        #self.correctionimage(direction)
        self.rect = self.image.get_rect()
        self.rect.x = self.owner.rect.center[0]
        self.rect.y = self.owner.rect.center[1]
        self.speed = 1
        self.time = pygame.time.get_ticks()
        self.knifecorrection(direction)
        self.timetodestroy = 150
        self.damage = 120

    def knifecorrection(self, direction):
        if direction == Direction.GORA:
            self.rect.y -= 40
        elif direction == Direction.PRAWO:
            self.rect.x += 10
        elif direction == Direction.DOL:
            self.rect.x -= 30
            self.rect.y += 10
        elif direction == Direction.LEWO:
            self.rect.x -= 40
            self.rect.y -= 30
        elif direction == Direction.GORALEWO:
            self.rect.x -= 20
            self.rect.y -= 40
        elif direction == Direction.GORAPRAWO:
            self.rect.x += 10
            self.rect.y -= 20
        elif direction == Direction.DOLLEWO:
            self.rect.x -= 40
            self.rect.y -= 10
        elif direction == Direction.DOLPRAWO:
            self.rect.x -= 10
            self.rect.y += 10


class PistolBlast(Blast):
    def __init__(self, owner, direction):
        super().__init__(owner)
        self.image = pygame.Surface([5, 5])
        self.image.fill(Color.RED.value)
        # self.correctionimage(direction)
        self.rect = self.image.get_rect()
        self.rect.x = self.owner.rect.center[0]
        self.rect.y = self.owner.rect.center[1]
        self.speed = 5
        self.time = pygame.time.get_ticks()
        self.correction(direction)
        self.timetodestroy = 1000
        self.damage = 100


class TompsonBlast(Blast):
    def __init__(self, owner, direction):
        super().__init__(owner)
        self.image = pygame.Surface([5, 5])
        self.image.fill(Color.RED.value)
        # self.correctionimage(direction)
        self.rect = self.image.get_rect()
        self.rect.x = self.owner.rect.center[0]
        self.rect.y = self.owner.rect.center[1]
        self.speed = 7
        self.time = pygame.time.get_ticks()
        self.correction(direction)
        self.timetodestroy = 2000
        self.damage = 200


class Mp40Blast(Blast):
    def __init__(self, owner, direction):
        super().__init__(owner)
        self.image = pygame.Surface([10, 10])
        self.image.fill(Color.RED.value)
        # self.correctionimage(direction)
        self.rect = self.image.get_rect()
        self.rect.x = self.owner.rect.center[0]
        self.rect.y = self.owner.rect.center[1]
        self.speed = 6
        self.time = pygame.time.get_ticks()
        self.correction(direction)
        self.timetodestroy = 3000
        self.damage = 300


