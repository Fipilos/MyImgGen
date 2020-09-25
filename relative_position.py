class RelativePosition(object):
    def __init__(self, left=0.0, top=0.0, right=1.0, bottom=1.0):
        """ each value from 0 to 1"""
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom

    def multiply(self, multiplier, direction):
        """ direction: {'x': 'left' or 'right', 'y': 'top' or 'bottom'} (to which box border)"""
        self.left = self.multiply_coord_into_direction(self.left, direction['x'], multiplier['x'])
        self.right = self.multiply_coord_into_direction(self.right, direction['x'], multiplier['x'])
        self.top = self.multiply_coord_into_direction(self.top, direction['y'], multiplier['y'])
        self.bottom = self.multiply_coord_into_direction(self.bottom, direction['y'], multiplier['y'])

    @staticmethod
    def multiply_coord_into_direction(coord, direction, multiplier):
        if direction in ['left', 'top']:
            multiplied_coord = coord * multiplier
        elif direction in ['right', 'bottom']:
            multiplied_coord = 1 - (1 - coord) * multiplier

        return multiplied_coord

    def __repr__(self):
        return str(self.__dict__)
