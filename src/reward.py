class Reward():
    def __init__(self):
        self.name = ""

    def set_reward_name(self, name):
        self.name = name

    def get_reward_message(self):
        return "Congratulations! You collected the " + self.name