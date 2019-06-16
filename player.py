from characters import Character
from textures import img


class Player(Character):
    """Klasa dla gracza"""
    def __init__(self):
        super().__init__()
        self.image = self.org_image = img.player
        self.hp = 100
        self.selectedgun = None
