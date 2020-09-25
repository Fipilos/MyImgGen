from spacy.lemmatizer import Lemmatizer
from spacy.lang.en import LEMMA_INDEX, LEMMA_EXC, LEMMA_RULES
lemmatizer = Lemmatizer(LEMMA_INDEX, LEMMA_EXC, LEMMA_RULES)


BASE_WORD = 'kisses'


def get_base_word(word, speech_part):
    base_word = lemmatizer(word, speech_part)

    return base_word


if __name__ == '__main__':
    print(get_base_word(BASE_WORD, 'NOUN'))