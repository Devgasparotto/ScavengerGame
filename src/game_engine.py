import arcade, time

MUSIC_VOLUME = 0.5

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
    
    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here
        
        arcade.start_render()

    def on_draw(self):
        """
        Render the screen.
        """
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        
        self.draw_runway()
        
    def draw_runway(self):
        arcade.draw_rectangle_filled(self.x/2, self.y/2, self.x/1.2, self.y, arcade.color.RED)
        #arcade.draw_rectangle_filled(self.x/2, self.y/2, self.x/1.2, self.y, arcade.color.RED)
        
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
        
        if key == arcade.key.A:
            self.green_is_pressed = True
        if key == arcade.key.S:
            self.red_is_pressed = True
        if key == arcade.key.D:
            self.yellow_is_pressed = True
        if key == arcade.key.F:
            self.blue_is_pressed = True
        if key == arcade.key.G:
            self.orange_is_pressed = True    

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