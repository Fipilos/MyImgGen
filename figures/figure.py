class Figure(object):
    def __init__(self, params):
        self.params = params

    def __repr__(self):
        return str(self.__dict__)
