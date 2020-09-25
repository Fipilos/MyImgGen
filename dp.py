from spacy import displacy
import spacy

from sentence import Sentence

# NLP = spacy.load('en_core_web_md')
NLP = spacy.load('en_core_web_sm')


while True:
    print('Write your sentence:')
    sentence_txt = input('')

    if sentence_txt.strip() == '':
        continue

    sentence = Sentence(sentence_txt, NLP)
    print(sentence)
    displacy.serve(sentence.doc, style='dep')
