from position.move_vector import MoveVector


class PositionPhrase(object):
    def __init__(self, subject=None, preposition=None, obj=None, verb=None):
        self.subject = subject
        self.preposition = preposition
        self.object = obj
        self.verb = verb

    def __repr__(self):
        return str(self.__dict__)

    def get_move_vector_for_attribute(self):
        """
        In future, it may depend on subject and object
        """
        if self.preposition == 'on':
            move = MoveVector(x=0, y=1)
        elif self.preposition == 'over':
            move = MoveVector(x=0, y=2)
        elif self.preposition == 'under':
            move = MoveVector(x=0, y=-1)
        elif self.preposition == 'below':
            move = MoveVector(x=0, y=-2)
        elif self.preposition == 'near':
            move = [MoveVector(x=-1, y=0), MoveVector(x=1, y=0)]
        else:
            raise ValueError('unknown preposition: {}'.format(self.preposition))

        return move

    def get_move_vector_for_objects_pair(self):
        """ todo use info from verb"""
        move = [MoveVector(x=-1, y=0), MoveVector(x=1, y=0)]

        return move

