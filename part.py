from relative_position import RelativePosition


class Part(object):
    def __init__(self, entity, relative_position=RelativePosition()):
        self.entity = entity
        self.relative_position = relative_position

    def __repr__(self):
        return str(self.__dict__)
