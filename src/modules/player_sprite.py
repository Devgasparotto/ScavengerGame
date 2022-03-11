from .player import Player
from arcade import Sprite

class PlayerSprite(Sprite):

    def __init__(self, image, scale, player_obj):
        super().__init__(image, scale)
        self.player = player_obj