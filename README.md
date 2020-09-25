# Description
Tool for generating simple images from any sentence in natural (English) language.

# Usage
`python main.py`
then after prompt write your sentence. The result will be saved in out.jpg file, then the loop will repeat with another prompt.

# Purpose

There is still a lot work to do, but after improving the tool, including user-friendly GUI, it can be useful for disabled people to understand the basic meaning of sentences.

# Limitations

- only single (one clause with single verb) sentences are supported
- all verbs will be treated as "be" verb i.e. they will only confirm the existence of subject in the image - to be changed
- if a noun or adjective is not known to the tool, it will be substituted by the most similar word - results will keep getting better, as more words are directly supported
- determiners ("a", "the", "these" etc.) are ignored

# Requirements

spacy==2.0.18
word2number==1.1
opencv-contrib-python==3.2.0.7
