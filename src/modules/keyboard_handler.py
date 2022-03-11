import arcade
from .player import Player


class KeyboardHandler():
    
    def __init__(self):
        pass

    def handle_character_movement(self, key: int, player: Player, pressed: bool = True):
        """
        function determines which keys are all pressed
        """
        if pressed:
            if key == arcade.key.W:
                player.move_up()
            if key == arcade.key.S:
                player.move_down()
            if key == arcade.key.A:
                player.move_left()
            if key == arcade.key.D:
                player.move_right()
                
        else:
            if key == arcade.key.W:
                player.set_velocity_y(0)
            if key == arcade.key.S:
                player.set_velocity_y(0)
            if key == arcade.key.A:
                player.set_velocity_x(0)
            if key == arcade.key.D:
                player.set_velocity_x(0)