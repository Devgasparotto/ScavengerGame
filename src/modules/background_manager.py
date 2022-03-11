from arcade import load_texture
class BGManager():

    def __init__(self, file):
        self.bg = file
    
    def load_bg(self):
        return load_texture(self.bg)