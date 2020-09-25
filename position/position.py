class Position(object):
    def __init__(self, left, top, right, bottom):
        self.left = left
        self.right = right
        self.bottom = bottom
        self.top = top

    def __eq__(self, another):
        return self.__dict__ == another.__dict__

    def __repr__(self):
        return str(self.__dict__)
