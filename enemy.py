import pygame
from characters import Character
from textures import img
from weapons import Pistol, Tompson, Mp40


class Enemy(Character):
    def __init__(self, x, y):
        super().__init__()
        self.rect.x = x
        self.rect.y = y
        self.last_attack = 0
        self.period = 0
        self.enemy = True
        self.pointsdamage = 0
        self.points = 0

    def damage(self, n):
        super().damage(n)
        if self.hp <= 0:
            self.kill()
            return True
        return False

    def attack(self, blasts):
        if pygame.time.get_ticks() - self.last_attack < self.period:
            return
        blasts.add(self.selectedgun.blast(self, self.direction))
        self.last_attack = pygame.time.get_ticks()

    def draw(self, screen):
        self.selectedgun.drawmini(self, screen)


class Enemy1(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = self.org_image = img.enemy1
        self.hp = 500
        self.selectedgun = Pistol(0, 0)
        self.period = 2000
        self.pointsdamage = 5
        self.points = 10


class Enemy2(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = self.org_image = img.enemy2
        self.hp = 1000
        self.selectedgun = Tompson(0, 0)
        self.period = 500
        self.pointsdamage = 7
        self.points = 20


class Enemy3(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = self.org_image = img.enemy3
        self.hp = 1500
        self.selectedgun = Mp40(0, 0)
        self.selectedgun.blast.speed = 12
        self.period = 500
        self.pointsdamage = 9
        self.points = 35
