from reward import Reward

class Collectable():
    def __init__(self, collectable_creation_input):
        self.x = collectable_creation_input.x
        self.y = collectable_creation_input.y
        self.size = collectable_creation_input.size
        self.is_collected = collectable_creation_input.is_collected

        self.reward = Reward()
        self.reward.set_reward_name(str(collectable_creation_input.name))

    def collect_item(self):
        self.is_collected = True
        return self.__get_reward()

    def __get_reward(self):
        return self.reward

class CollectableCreationInput():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 0
        self.is_collected = False
        self.name = ""