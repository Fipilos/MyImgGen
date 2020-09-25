import config as cfg

from time import time


def _get_similarity(a, b):
    similarity = a.similarity(b)

    return similarity


def find_most_similar(name, speech_part='noun'):
    token = cfg.NLP(name)
    most_similar = max(cfg.TOKENS[speech_part], key=lambda x: _get_similarity(x, token))

    if speech_part == 'adj':
        most_similar = str(most_similar)

    return most_similar


if __name__ == '__main__':
    print(time())
    name = 'animal'
    most_similar = find_most_similar(name)
    print(most_similar)

    print(time())
    name = 'dog'
    print(find_most_similar(name))
    print(time())

    print(find_most_similar('huge', 'adj'))
