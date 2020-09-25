from importlib import import_module

from entity_parameters import EntityParameters as EP
from hierarchy.common import choose_type
from hierarchy.data import TYPES, SYN
from grammar.lemmas import get_base_noun
import config as cfg
from hierarchy.similarity import find_most_similar


def _get_capital_word(word):
    capital_word = word[0].upper() + word[1:]

    return capital_word


def _get_entity_type(noun):
    singular = _get_entity_singular(noun)

    entity_name = _get_capital_word(singular)
    entity_module = import_module('entities.' + singular)
    entity_type = getattr(entity_module, entity_name)

    return entity_type


def _get_entity_singular(noun):
    if noun in SYN:
        noun = SYN[noun]

    if noun in cfg.NAMES:
        singular = noun
    elif noun in TYPES:
        singular = choose_type(TYPES[noun])
    else:
        singular = get_base_noun(noun)

        if singular:
            singular = _get_entity_singular(singular)
        else:
            singular = _get_entity_type_for_unknown_noun(noun)

    return singular


def _get_entity_type_for_unknown_noun(noun):
    """
    todo prepare
    """
    print('Unknown noun: {}.'.format(noun))
    most_similar = find_most_similar(noun).text
    print(f'Creating {most_similar} instead.')

    return most_similar


def create_entities(noun_phrase):
    entities = []

    for _ in range(noun_phrase.cnt):
        entity_type = _get_entity_type(noun_phrase.root.lemma_)

        if entity_type is None:
            return None

        parameters = {EP.ID: noun_phrase.id_, EP.ATTRIBUTES: set()}
        entity = entity_type(parameters)
        entity.apply_determiners(noun_phrase.determiners)
        entity.apply_modifiers(noun_phrase.modifiers)

        if noun_phrase.mod_verb is not None:
            mod_verb = noun_phrase.mod_verb
            entity.apply_mod_verb(mod_verb)

        entities.append(entity)

    return entities
