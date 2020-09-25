class NounPhraseList(object):
    def __init__(self, noun_phrase_list):
        self.noun_phrase_list = noun_phrase_list

    def __repr__(self):
        return ';'.join([str(i) for i in self.noun_phrase_list])
