from time import time

from sentence import Sentence
from grammatical_world import GrammaticalWorld
from logical_world import LogicalWorld
import config as cfg
from draw import Draw


def get_logical_world(sentence_txt):
    sentence = Sentence(sentence_txt, cfg.NLP)
    print('Text: {}'.format(sentence))

    grammatical_objects = sentence.get_grammatical_objects()
    subject = sentence.get_subjects()
    grammatical_object_pairs = sentence.get_grammatical_object_pairs()
    attributes = sentence.get_attributes()
    grammatical_world = GrammaticalWorld(subjects=subject,
                                         objects=grammatical_objects,
                                         objects_pairs=grammatical_object_pairs,
                                         attributes=attributes)
    print('Grammatical world: {}'.format(grammatical_world))
    logical_world = LogicalWorld(grammatical_world)
    print('Logical world: {}'.format(logical_world))
    # logical_world.print_positioned_entities()

    return logical_world


if __name__ == '__main__':
    while True:
        print('Write your sentence:')
        sentence_txt = input('')

        if sentence_txt.strip() == '':
            continue

        try:
            sentence = Sentence(sentence_txt, cfg.NLP)
            # print('Text: {}'.format(sentence))

            grammatical_objects = sentence.get_grammatical_objects()
            subjects = sentence.get_subjects()
            grammatical_object_pairs = sentence.get_grammatical_object_pairs()
            attributes = sentence.get_attributes()
            grammatical_world = GrammaticalWorld(subjects=subjects,
                                                 objects=grammatical_objects,
                                                 objects_pairs=grammatical_object_pairs,
                                                 attributes=attributes)
            print('Grammatical world: {}'.format(grammatical_world))
            logical_world = LogicalWorld(grammatical_world)
            # print('Logical world: {}'.format(logical_world))
            draw = Draw(logical_world)
            img = draw.draw(save=True, display=False)
        except Exception as e:
            print(e)
