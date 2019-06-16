import pygame
import pygame.gfxdraw


class Blast(pygame.sprite.Sprite):
    def __init__(self, owner):
        super().__init__()
        self.owner = owner


class KnifeBlast(Blast):
    def __init__(self, owner, vector):
        super().__init__(owner)
        self.image = pygame.Surface([20, 20])
        self.image.fill((100, 200, 200))
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 20
        self.speed = 1
        self.time = pygame.time.get_ticks()
        self.vector = vector

    def update(self):
        if self.time is not None:
            if pygame.time.get_ticks() - self.time >= 20:
                self.kill()
        self.rect.x += self.vector[0]
        self.rect.y += self.vector[1]
