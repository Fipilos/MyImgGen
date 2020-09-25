from grammar.noun_phrase import NounPhrase


class PrepPhrase(object):
    def __init__(self, root, obj_cnt):
        self.root = root
        self.noun_phrase = None
        self._parse(obj_cnt)

    def __repr__(self):
        return str(self.__dict__)

    def _parse(self, obj_cnt):
        for descendant in self.root.children:
            if descendant.dep_ == 'pobj':
                self.noun_phrase = NounPhrase(descendant, obj_cnt)
            elif descendant.dep_ == 'punct':
                'todo'
            else:
                print('{} is unknown dep_ for {}: {}'.format(descendant, self.root, descendant.dep_))