
class Player():

    def __init__(self, x, y):
        self.velocity_x = 0
        self.velocity_y = 0
        self.speed = 200
        self.x = x
        self.y = y

    def set_velocity_x(self, velocity):
        self.velocity_x = velocity
    
    def set_velocity_y(self, velocity):
        self.velocity_y = velocity
    
    def move_character_by_velocity(self, delta_time):
        self.__move_x_axis(delta_time)
        self.__move_y_axis(delta_time)

    def __move_x_axis(self, delta_time):
        self.x += self.velocity_x * delta_time

    def __move_y_axis(self, delta_time):
        self.y += self.velocity_y * delta_time
    
    def move_up(self):
        self.set_velocity_y(self.speed * 1)
    
    def move_down(self):
        self.set_velocity_y(self.speed * -1)
    
    def move_left(self):
        self.set_velocity_x(self.speed * -1)
    
    def move_right(self):
        self.set_velocity_x(self.speed * 1)
    
    def draw(self, sprite_object):
        sprite_object.draw()

    def update(self, delta_time, sprite_object):
        self.move_character_by_velocity(delta_time)
        sprite_object.set_position(self.x, self.y)