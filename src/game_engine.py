from player import Player
from typing import Optional
import arcade, time

MUSIC_VOLUME = 0.5
TILE_SCALING = 0.5

class GameEngine(arcade.Window):
    def __init__(self, width, height, title):
        self.x, self.y = width,height
        
        super().__init__(width, height, title)
        
        arcade.set_background_color(arcade.color.AMAZON)
        
        self.green_is_pressed = False
        self.red_is_pressed = False
        self.yellow_is_pressed = False
        self.blue_is_pressed = False
        self.orange_is_pressed = False

        self.player = None
        #self.tile_map = None

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        
        # Create player
        self.player = Player(100, 100)

        arcade.start_render()

        map_name = ":resources:tiled_maps/map.json"

        #map_name = ":resources:tiled_maps/map1.json"

        layer_options = {
            "Platforms": {
                "use_spatial_hash": True,
            },
        }

        # Read in the tiled map
        self.tile_map = arcade.load_tilemap(map_name, TILE_SCALING, layer_options)

        self.scene = arcade.Scene.from_tilemap(self.tile_map)

    def on_draw(self):
        """
        Render the screen.
        """
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()
        self.draw_background()
        self.draw_player()
        # Draw our Scene
        self.scene.draw()
        
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
        pass

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        pass
        
        # TODO: Add room border logic
        # TODO: Add hold move logic
        if key == arcade.key.W:
            self.player.move_up()
        if key == arcade.key.S:
            self.player.move_down()
        if key == arcade.key.A:
            self.player.move_left()
        if key == arcade.key.D:
            self.player.move_right()

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        if key == arcade.key.A: # green
            self.green_is_pressed = False
        if key == arcade.key.S:
            self.red_is_pressed = False
        if key == arcade.key.D:
            self.yellow_is_pressed = False
        if key == arcade.key.F:
            self.blue_is_pressed = False
        if key == arcade.key.G:
            self.orange_is_pressed = False

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