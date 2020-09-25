"""
Pair of noun phrases (e.g subject and object) with relations between them
"""


class NpPair(object):
    def __init__(self, first_np, second_np, verb):
        self.first_np = first_np
        self.second_np = second_np
        self.verb = verb

    def __repr__(self):
        return str(self.__dict__)