from grammar.adjective_phrase import AdjectivePhrase
from numerals import get_number_from_numeral
from exceptions import ParseError


class NounPhrase(object):
    def __init__(self, root, id_, mod_verb=None):
        self.root = root
        self.modifiers = []
        self.determiners = []
        self.mod_verb = mod_verb
        self.id_ = id_
        self.cnt = 1
        self._parse()

    def __repr__(self):
        return str(self.__dict__)

    def _parse(self):
        for descendant in self.root.children:
            if descendant.dep_ == 'det':
                self.determiners.append(descendant)
            elif descendant.dep_ == 'amod':
                self.modifiers.append(AdjectivePhrase(descendant))
            elif descendant.dep_ == 'punct':
                'todo'
            elif descendant.dep_ == 'acl':
                self.modifiers.append(AdjectivePhrase(descendant))
            elif descendant.dep_ == 'nummod':
                self.cnt = get_number_from_numeral(descendant)
            elif descendant.dep_ in {'cc', 'conj'}:
                'should be already done'
            else:
                raise(ParseError('{} is unknown dep_ for {}: {}'.format(descendant, self.root, descendant.dep_)))
