from collectable import Collectable, CollectableCreationInput

import arcade
import logging

class CollectablesManager():
    def __init__(self):
        self.collectables_list = []
        self.__initialize_collectables()

    def draw_collectables(self, game_engine_arcade):
        # NOTE: game_engine_arcade AND base arcade variables could work here.
        # I am choosing to use game_engine_arcade as this may help to ensure better interaction
        
        for c in self.collectables_list:
            game_engine_arcade.draw_rectangle_filled(c.x, c.y, c.size, c.size, arcade.color.RED)
    
    
    def __initialize_collectables(self):
        logging.info("Initializing Collectables")
        collectable_input1 = CollectableCreationInput()
        collectable_input1.x = 300
        collectable_input1.y = 300
        collectable_input1.size = 5
        collectable_input1.name = "First Item"
        collectable1 = Collectable(collectable_input1)
        self.collectables_list.append(collectable1)
        

