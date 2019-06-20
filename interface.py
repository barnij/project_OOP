from enums import Squares, Direction, Color
import pygame
from abc import ABC, abstractmethod
from textures import img
from otherfunctions import rot_center


def draw_numbers(screen):
    screen.blit(img.numbersofweapons, (0, 0))


def draw_background(screen):
    screen.blit(img.background, (0, 0))


class Interface(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def draw(self, screen):
        pass


class Square(Interface):
    def __init__(self, cord: tuple):
        super().__init__()
        self.gun = None
        self.cord = cord
        self.image = None
        self.selected = False
        self.active = False

    def add_gun(self, gun):
        self.gun = gun
        self.image = gun.square

    def delete_gun(self):
        self.gun = self.image = None

    def draw(self, screen):
        if self.selected:
            screen.blit(img.chooseweapon, self.cord)
        if self.active:
            screen.blit(self.image, (0, 0))


class HealthBar(Interface):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.maxwidth = 300
        self.image = pygame.Surface([self.maxwidth, 40])
        self.rect = self.image.get_rect()
        self.x = 450
        self.y = 610

    def draw(self, screen):
        self.update()
        color = Color.GREEN.value
        hp = self.player.hp
        maxhp = self.player.maxhp
        if hp < maxhp*0.3:
            color = Color.RED.value
        elif hp < maxhp*0.5:
            color = Color.ORANGE.value
        elif hp < maxhp*0.7:
            color = Color.YELLOW.value
        pygame.draw.rect(screen, color, self.rect)

    def update(self):
        width = self.player.hp/self.player.maxhp * self.maxwidth
        self.image = pygame.Surface([width, 40])
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class ManageInterface:
    def __init__(self, player):
        self.squares = [Square(x.value) for x in Squares]
        self.select_square(0, player)
        self.healthbar = HealthBar(player)
        self.selected_square = 0
        self.last_attack = 0

    def make_active_square(self, i):
        self.squares[i].active = True

    def get_actual_square(self):
        return self.squares[self.selected_square]

    def select_square(self, i, player):
        for t in self.squares:
            t.selected = False
        self.squares[i].selected = True
        self.selected_square = i
        player.selectedgun = self.squares[i].gun

    def add_gun(self, gun, i):
        self.squares[i].gun = gun
        self.squares[i].image = gun.square

    def draw(self, screen, player):
        draw_background(screen)
        for i in self.squares:
            i.draw(screen)
        draw_numbers(screen)

        square = self.get_actual_square()
        if square.active:
            gun = square.gun
            x = player.rect.x - 5
            y = player.rect.y - 5
            d = player.direction.value
            g = gun.mini
            i = None

            if d is Direction.LEWO.value:
                i = rot_center(g, 90)
            elif d is Direction.PRAWO.value:
                i = rot_center(g, -90)
            elif d is Direction.GORA.value:
                i = rot_center(g, 0)
            elif d is Direction.DOL.value:
                i = rot_center(g, 180)
            elif d is Direction.GORAPRAWO.value:
                i = rot_center(g, -45)
            elif d is Direction.GORALEWO.value:
                i = rot_center(g, 45)
            elif d is Direction.DOLLEWO.value:
                i = rot_center(g, 135)
            elif d is Direction.DOLPRAWO.value:
                i = rot_center(g, -135)

            screen.blit(i, (x, y))

        self.healthbar.draw(screen)
