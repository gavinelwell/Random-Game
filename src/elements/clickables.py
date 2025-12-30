class Clickable:
    def __init__(self, pos, dimensions, color):
        self.pos = pos
        self.dimensions = dimensions
        self.color = color
    
    def __iter__(self):
        return iter(self)

    def in_boundary(self, coordinates) -> bool:
        '''
        Determines if a coordinate pair is within the bounds of the Clickable
        
        :param coordinates: Checked coordinate pair, often a mouse position
        :return: If the coordinate pair is within the given bounds
        :rtype: bool
        '''
        pass

import math
import random
class Target(Clickable):

    # For a target, self.dimensions is an int representing the radius
    # The center of the Target is self.pos
    def __init__(self, pos, dimensions, color):
        super().__init__(pos, dimensions, color)
    
    def in_boundary(self, coordinates) -> bool:
        bounds_x = coordinates[0] - self.pos[0]
        bounds_y = coordinates[1] - self.pos[1]
        return math.sqrt(bounds_x**2 + bounds_y**2) <= self.dimensions
    
    def hit(self, border):
        '''
        Randomly chooses a new Target position within the border
        
        :param border Tuple(int, int, int, int): Boundaries for the Target to be in (x0, x1, y0, y1)
        '''
        self.pos = (random.randint(border[0], border[1]), random.randint(border[2], border[3]))


class Button(Clickable):

    # For a button, self.dimensions is a tuple of ints representing the width and height
    # The bottom left corner of the Button is self.pos
    def __init__(self, pos, dimensions, color, text):
        super().__init__(pos, dimensions, color)
        self.rect = (pos[0], pos[1], dimensions[0], dimensions[1])
        self.text = text
    
    def in_boundary(self, coordinates) -> bool:
        in_bounds_x = 0 <= coordinates[0] - self.rect[0] <= self.rect[2]
        in_bounds_y = 0 <= coordinates[1] - self.rect[1] <= self.rect[3]
        return in_bounds_x and in_bounds_y