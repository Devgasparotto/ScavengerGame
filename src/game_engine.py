import arcade, time
from modules import *

MUSIC_VOLUME = 0.5

class GameEngine(arcade.Window):
    def __init__(self, width, height, title):
        self.x, self.y = width,height
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)
        self.keyboard_handler = KeyboardHandler()

        self.player = None
    
    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here
        
        # Create player
        self.player = Player(100, 100)

        arcade.start_render()

    def on_draw(self):
        """
        Render the screen.
        """
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()
        self.draw_background()
        self.draw_player()
        
    def draw_background(self):
        arcade.draw_rectangle_filled(self.x, 0, 0, self.y, arcade.color.AMAZON)


    def draw_player(self):
        # TODO: To move player size into player class

        arcade.draw_rectangle_filled(self.player.x, self.player.y, 8, 8, arcade.color.BLUE)
        
    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.player.move_character_by_velocity(delta_time)

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        self.keyboard_handler.handle_character_movement(key, self.player, pressed = True)

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        self.keyboard_handler.handle_character_movement(key, self.player, pressed = False)

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass