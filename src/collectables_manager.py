from collectable import Collectable, CollectableCreationInput

import arcade, random
import logging

class CollectablesManager():
    def __init__(self):
        self.collectables_list = arcade.SpriteList()
        self.__initialize_collectables()

    def draw_collectables(self, game_engine_arcade):
        # NOTE: both game_engine_arcade AND base arcade variables could work here.
        # I am choosing to use game_engine_arcade as this may help to ensure better interaction
        
        for c in self.collectables_list:
            if not c.is_collected:
                game_engine_arcade.draw_rectangle_filled(c.center_x, c.center_y, c.width, c.height, arcade.color.RED)

    def check_for_player_collision(self, game_engine_arcade, player_sprite):
        reward = None
        for c in self.collectables_list:
            if not c.is_collected:
                if game_engine_arcade.check_for_collision(player_sprite, c):
                    reward = c.collect_item()
                    
        return reward

    
    
    def __initialize_collectables(self):
        logging.info("Initializing Collectables")
        for i in range(0, 10):
            collectable_input1 = CollectableCreationInput()
            collectable_input1.x = random.randint(0,1000)
            collectable_input1.y = random.randint(0,1000)
            collectable_input1.size = 25
            collectable_input1.name = "Gasoline"
            collectable1 = Collectable('images/jerry_can.png', 1, collectable_input1)
            self.collectables_list.append(collectable1)
