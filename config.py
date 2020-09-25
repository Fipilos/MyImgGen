import spacy


CANVAS_HEIGHT = 360
CANVAS_WIDTH = 640
CANVAS_COLOR = (255, 255, 255)
OUTPUT_IMG_PATH = 'out.jpg'
NLP = spacy.load('en_core_web_md')
# NLP = spacy.load('en_core_web_sm')
LINE_COLOR = 'black'
LINE_THICKNESS = 4
COLOR = {'red': (0, 0, 255), 'blue': (255, 0, 0), 'white': (255, 255, 255), 'black': (0, 0, 0), 'green': (0, 255, 0), 'yellow': (0, 255, 255)}

# you can get this by running utils/names.py
NAMES = ['arm', 'cat', 'ear', 'entity', 'eye', 'face', 'hair', 'head', 'leg', 'man', 'mouth', 'nose', 'oval', 'table', 'tail', 'torso', 'trapezoid', 'triangle', 'woman']
ADJ = {'color': ['black', 'green', 'red', 'yellow', 'blue'], 'size': ['small', 'big', 'large', 'short', 'high', 'wide', 'narrow']}
ALL_ADJ = sum(ADJ.values(), [])

TOKENS = {'noun': NLP(' '.join(NAMES)), 'adj': NLP(' '.join(ALL_ADJ))}
