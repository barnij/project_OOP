from characters import Character
from textures import img


class Player(Character):
    """Klasa dla gracza"""
    def __init__(self):
        super().__init__()
        self.image = self.org_image = img.player
        self.selectedgun = None

    def damage(self, n):
        super().damage(n)
        return True if self.hp <= 0 else False
