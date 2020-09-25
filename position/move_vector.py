class MoveVector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return MoveVector(x=self.x + other.x,
                          y=self.y + other.y)

    def __repr__(self):
        return str(self.__dict__)
