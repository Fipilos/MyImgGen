from itertools import combinations

from grammar.np_pair import NpPair
from grammar.adverbial_phrase import AdverbialPhrase
from grammar.verb_phrase import VerbPhrase
from grammar.noun_phrase import NounPhrase
from grammar.prep_phrase import PrepPhrase
from grammar.adjective_phrase import AdjectivePhrase


class Sentence(object):
    def __init__(self, char_string, nlp):
        self.char_string = char_string
        self.root = None
        self.subjects = []
        self.objects = []
        self.nlp = nlp
        self.doc = None
        self.root_verb_phrase = None
        self.prep_phrases = []
        self.noun_phrases = []
        self.obj_cnt = 0
        self.verb_objects = []
        self.subject_idx = None
        self._parse()

    def __repr__(self):
        return str(self.__dict__)

    def _parse(self):
        self._set_doc()
        self._set_root()
        self._decide_which_root_child_is_subject()
        self._set_sentence_parts()
        self._set_subjects()

    def _decide_which_root_child_is_subject(self):
        for i, obj in enumerate(list(self.root.lefts) + list(self.root.rights)):
            if self._check_if_root_child_could_be_subject(obj):
                break
        else:
            raise(Exception('No subject in sentence!'))

        self.subject_idx = i

    @staticmethod
    def _check_if_root_child_could_be_subject(obj):
        if obj.tag_ not in ['NN', 'NNP', 'NNS']:
            return False

        if obj.dep_ in ['nsubj', 'attr']:
            return True
        else:
            return False

    def get_grammatical_objects(self):
        """
        Gets all objects that will be parts of the world
        """
        return self.objects

    def get_subjects(self):
        return self.subjects

    def get_grammatical_object_pairs(self):
        pairs = []

        for s in self.subjects:
            if s.mod_verb is None:
                for obj in self.objects:
                        pairs.append(NpPair(
                            first_np=s,
                            second_np=obj,
                            verb=self.root_verb_phrase
                          ))

        for subject_a, subject_b in combinations(self.subjects, 2):
            pairs.append(NpPair(first_np=subject_a, second_np=subject_b, verb=None))

        return pairs

    def get_attributes(self):
        return self.prep_phrases

    def get_world_attributes(self):
        'todo'

    def _set_subjects(self):
        root = (list(self.root.lefts) + list(self.root.rights))[self.subject_idx]
        if self.root_verb_phrase.objects:
            mod_verb = None
        else:
            mod_verb = self.root_verb_phrase

        self._add_objects(root, mod_verb=mod_verb, is_subject=True)

    def _set_doc(self):
        self.char_string = self.char_string.strip()
        self.char_string = ' '.join(self.char_string.split())
        self.doc = self.nlp(self.char_string)
        for t in self.doc:
            print(t, t.dep_, t.tag_, [(c, c.dep_, c.tag_) for c in t.children])

    def _set_root(self):
        root = [token for token in self.doc if token.head == token][0]

        if root.tag_ in {'VB', 'VBD', 'VBP', 'VBZ'}:
            self.root = root
        elif root.tag_ in {'NN', 'NNP', 'NNS'}:
            self._add_verb_to_charstring(root.text)
            print(f'No verb found, the sentence changed into {self.char_string}')
            self._set_doc()
            self._set_root()

    def _add_verb_to_charstring(self, subject):
        if self.char_string.startswith(subject):
            to_replace = subject + ' '
        else:
            to_replace = ' ' + subject + ' '

        self.char_string = self.char_string.replace(to_replace, ' ' + subject + ' is ', 1)

    def _set_sentence_parts(self):
        adv_modifiers = []
        particles = []
        adj_complements = []
        attributes = []

        for i, obj in enumerate(list(self.root.lefts) + list(self.root.rights)):
            if i == self.subject_idx:
                continue

            if obj.dep_ == 'prep':
                self.prep_phrases.append(PrepPhrase(obj, self.obj_cnt))
                self.obj_cnt += 1
            elif obj.dep_ == 'prt':
                particles.append(obj)
            elif obj.dep_ in ['obj', 'dobj', 'dative']:
                self._add_objects(obj, mod_verb=None, is_subject=False)
            elif obj.dep_ in ['advcl', 'acl', 'advmod']:
                adv_modifiers.append(AdverbialPhrase(obj))
            elif obj.dep_ == 'acomp':
                adj_complements.append(AdjectivePhrase(obj))
            elif obj.dep_ == 'attr':
                attributes.append(obj)
            elif obj.dep_ in ['nsubj', 'expl']:
                print(f'Ignoring word {obj.text}')
            else:
                print('{} is unknown dep_ for {}: {}'.format(obj, self.root, obj.dep_))
        self.root_verb_phrase = VerbPhrase(verb=self.root,
                                           objects=self.verb_objects,
                                           adv_modifiers=adv_modifiers,
                                           particles=particles,
                                           adj_complements=adj_complements,
                                           attributes=attributes)

    @staticmethod
    def _check_if_is_and_in_children(obj):
        for c in obj.children:
            if c.text == 'and':
                return True

        return False

    def _add_objects(self, obj, mod_verb, is_subject):
        if is_subject:
            self.subjects.append(NounPhrase(obj, id_=self.obj_cnt, mod_verb=mod_verb))
        else:
            self.objects.append(NounPhrase(obj, id_=self.obj_cnt, mod_verb=mod_verb))
            self.verb_objects.append(obj)

        self.obj_cnt += 1

        if self._check_if_is_and_in_children(obj):
            for c in obj.children:
                if c.dep_ == 'conj':
                    self._add_objects(c, mod_verb, is_subject)
