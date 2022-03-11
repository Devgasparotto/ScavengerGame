class Player():
    def __init__(self, x, y):
        self.speed = 10
        self.x = x
        self.y = y
        
    
    def move_up(self):
        self.y += self.speed

    def move_down(self):
        self.y -= self.speed

    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed
    