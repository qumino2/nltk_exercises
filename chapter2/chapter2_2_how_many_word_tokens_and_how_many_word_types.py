from nltk.corpus import gutenberg, brown, state_union
from nltk.corpus import wordnet as wn

print len(gutenberg.words('austen-persuasion.txt'))

print len(set(word.lower() for word in gutenberg.words('austen-persuasion.txt')))
