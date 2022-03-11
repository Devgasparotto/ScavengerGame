from collectable import Collectable, CollectableCreationInput

import arcade
import logging

class CollectablesManager():
    def __init__(self):
        self.collectables_list = []
        self.__initialize_collectables()

    def draw_collectables(self, game_engine_arcade):
        # NOTE: both game_engine_arcade AND base arcade variables could work here.
        # I am choosing to use game_engine_arcade as this may help to ensure better interaction
        
        for c in self.collectables_list:
            if not c.is_collected:
                game_engine_arcade.draw_rectangle_filled(c.center_x, c.center_y, c.width, c.height, arcade.color.RED)

    def check_for_player_collision(self, game_engine_arcade, player_sprite):
        for c in self.collectables_list:
            if not c.is_collected:
                if game_engine_arcade.check_for_collision(player_sprite, c):
                    print("Touching")
                    #c.collect_item()
                    #logging.info(c.name + " has been collected.")

    
    
    def __initialize_collectables(self):
        logging.info("Initializing Collectables")
        collectable_input1 = CollectableCreationInput()
        collectable_input1.x = 200
        collectable_input1.y = 200
        collectable_input1.size = 25
        collectable_input1.name = "First Item"
        collectable1 = Collectable(collectable_input1)
        self.collectables_list.append(collectable1)
        

