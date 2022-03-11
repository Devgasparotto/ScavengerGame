import arcade, time
from modules import *

MUSIC_VOLUME = 0.5

class GameEngine(arcade.Window):
    def __init__(self, width, height, title):
        self.x, self.y = width,height
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)
        self.keyboard_handler = KeyboardHandler()
        self.player_sprite_list = arcade.SpriteList()
        self.player = None
    
    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here
        
        # Create player
        self.player = Player(100, 100)
        self.sprite_for_player = PlayerSprite("images/player.png", 0.2, self.player)

        arcade.start_render()

    def on_draw(self):
        """
        Render the screen.
        """
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()
        self.draw_background()
        self.player.draw(self.sprite_for_player)
        
    def draw_background(self):
        arcade.draw_rectangle_filled(self.x, 0, 0, self.y, arcade.color.AMAZON)
        
    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.player.update(delta_time, self.sprite_for_player)

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