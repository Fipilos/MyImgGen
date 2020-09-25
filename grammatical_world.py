class GrammaticalWorld(object):
    def __init__(self, subjects, objects, objects_pairs, attributes=None):
        self.subjects = subjects
        self.objects = objects
        self.objects_pairs = objects_pairs
        self.attributes = attributes
        self._create_object_from_attributes()

    def __repr__(self):
        return str(self.__dict__)

    def _create_object_from_attributes(self):
        for attr in self.attributes:
            if attr.noun_phrase is not None:
                self.objects.append(attr.noun_phrase)
