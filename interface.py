from enums import Squares, Direction, Color
import pygame
from abc import ABC, abstractmethod
from textures import img
from settings import ARENAHEIGHT, ARENAWIDTH
from weapons import Knife, Pistol, Tompson, Mp40


pygame.font.init()
myfont = pygame.font.Font('font/Terminus.ttf', 30)


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
        self.ammo = 0

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
        self.x = 420
        self.y = 607

    def draw(self, screen, end=False):
        if end:
            self.update(True)
            color = Color.BLACK.value
        else:
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
        screen.blit(img.healthbar, (self.x - 2, self.y - 2))

    def update(self, end=False):
        if end:
            self.image = pygame.Surface([self.maxwidth, 40])
            self.rect = self.image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y
        else:
            width = self.player.hp/self.player.maxhp * self.maxwidth
            self.image = pygame.Surface([width, 40])
            self.rect = self.image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y


class PointsCounter(Interface):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.counter = 0

    def draw(self, screen):
        textsurface = myfont.render(str(self.counter)+" points", False, Color.WHITE.value)
        screen.blit(textsurface, (780, 610))


class AmmoStatus(Interface):
    def __init__(self):
        super().__init__()
        self.value = 0

    def draw(self, screen):
        textsurface = myfont.render(str(self.value)+" ammo left", False, Color.WHITE.value)
        screen.blit(textsurface, (780, 650))

    def updateanddraw(self, n, screen):
        self.value = n
        self.draw(screen)


class ManageInterface:
    def __init__(self, player):
        self.squares = [Square(x.value) for x in Squares]
        self.init_squares()
        self.select_square(0, player)
        self.healthbar = HealthBar(player)
        self.points = PointsCounter(player)
        self.ammo = AmmoStatus()
        self.selected_square = 0
        self.last_attack = 0
        self.roundtext = 0

    def make_active_square(self, i):
        self.squares[i].active = True

    def get_actual_square(self):
        return self.squares[self.selected_square]

    def get_square_with_gun(self, gun):
        gun = gun.__class__.__name__
        if gun == 'Knife':
            return self.squares[0]
        elif gun == 'Pistol':
            return self.squares[1]
        elif gun == 'Tompson':
            return self.squares[2]
        elif gun == 'Mp40':
            return self.squares[3]
        return False

    def select_square(self, i, player):
        for t in self.squares:
            t.selected = False
        self.squares[i].selected = True
        self.selected_square = i
        player.selectedgun = self.squares[i].gun

    def init_squares(self):
        self.add_gun(Knife(0, 0), 0)
        self.add_gun(Pistol(0, 0), 1)
        self.add_gun(Tompson(0, 0), 2)
        self.add_gun(Mp40(0, 0), 3)

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
            square.gun.drawmini(player, screen)

        self.healthbar.draw(screen)
        self.points.draw(screen)
        self.ammo.updateanddraw(self.get_actual_square().ammo, screen)
        self.drawround(screen)

    def addpoints(self, n):
        self.points.counter += n

    def gameover(self, screen):
        screen.blit(img.gameover, (ARENAWIDTH//2-150, ARENAHEIGHT//2-100))

    def win(self, screen):
        screen.blit(img.win, (ARENAWIDTH//2-150, ARENAHEIGHT//2-100))

    def drawround(self, screen):
        textsurface = myfont.render(str(self.roundtext), False, Color.WHITE.value)
        screen.blit(textsurface, (600, 650))
