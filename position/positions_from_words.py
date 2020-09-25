from position.position_phrase import PositionPhrase
from entity_parameters import EntityParameters as EP


def get_position_phrase_for_single_attribute(subject, single_attribute):
    """ assuming attribute.root is preposition..."""
    pos_phrase = PositionPhrase(subject=subject,
                                obj=single_attribute.noun_phrase,
                                preposition=single_attribute.root.text)
    return pos_phrase


def get_position_phrase_for_objects_pair(objects_pair):
    pos_phrase = PositionPhrase(subject=objects_pair.first_np,
                                obj=objects_pair.second_np,
                                verb=objects_pair.verb)

    return pos_phrase


def get_relative_position_for_single_attribute(subject, single_attribute):
    pos_phrase = get_position_phrase_for_single_attribute(subject, single_attribute)
    move_vector = pos_phrase.get_move_vector_for_attribute()

    return move_vector


def get_relative_position_for_pos_phrase(pos_phrase):
    move_vector = pos_phrase.get_move_vector_for_objects_pair()

    return move_vector


def get_position_phrases(subject, attributes):
    pos_phrases = []

    for attr in attributes:
        pos_phrases.append(get_position_phrase_for_single_attribute(subject, attr))

    return pos_phrases


def get_rel_pos_dict(subjects, attributes, objects_pairs):
    rel_pos_dict = dict()

    for s in subjects:
        for attr in attributes:
            rel_pos_dict[(s.id_, attr.noun_phrase.id_)] = get_relative_position_for_single_attribute(s, attr)

    for op in objects_pairs:
        rel_pos_dict[(op.first_np.id_, op.second_np.id_)] = get_position_phrase_for_objects_pair(op)

    return rel_pos_dict



