import pygame
from enemy import Enemy1, Enemy2, Enemy3
from weapons import Knife, Pistol, Tompson, Mp40


class Round:
    def __init__(self, player):
        self.enemies_group = pygame.sprite.Group()
        self.blasts_group = pygame.sprite.Group()
        self.characters_group = pygame.sprite.Group()
        self.characters_group.add(player)
        self.available_weapons = []
        self.points_of_spawn = []
        self.all_blasts_list = []
        self.time_to_spawn_weapon = 0
        self.last_spawn_weapon = 0
        self.next_round = None
        self.text = ""

    def ifnextround(self):
        if len(self.enemies_group) == 0:
            return True


class Round1(Round):
    def __init__(self, player):
        super().__init__(player)
        self.list_of_enemies = [Enemy1(20, 20), Enemy1(80, 20), Enemy1(200, 20), Enemy1(300, 20)]
        for x in self.list_of_enemies:
            self.characters_group.add(x)
            self.enemies_group.add(x)
        self.available_weapons = [Knife, Pistol]
        self.next_round = Round2(player)
        self.time_to_spawn_weapon = 7000
        self.text = "round 1"


class Round2(Round):
    def __init__(self, player):
        super().__init__(player)
        self.list_of_enemies = [Enemy2(20, 20), Enemy2(80, 20), Enemy2(200, 20), Enemy1(300, 20), Enemy1(700, 500)]
        for x in self.list_of_enemies:
            self.characters_group.add(x)
            self.enemies_group.add(x)
        self.available_weapons = [Knife, Pistol, Tompson]
        self.next_round = Round3(player)
        self.time_to_spawn_weapon = 5000
        self.text = "round 2"


class Round3(Round):
    def __init__(self, player):
        super().__init__(player)
        self.list_of_enemies = [Enemy3(20, 20), Enemy3(80, 20), Enemy2(200, 20), Enemy1(300, 20), Enemy1(700, 500)]
        for x in self.list_of_enemies:
            self.characters_group.add(x)
            self.enemies_group.add(x)
        self.available_weapons = [Knife, Pistol, Mp40]
        self.time_to_spawn_weapon = 9000
        self.next_round = None
        self.text = "round 3"
