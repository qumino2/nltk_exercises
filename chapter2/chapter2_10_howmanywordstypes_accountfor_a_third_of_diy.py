import nltk
from nltk.book import*
from __future__ import division

def percentage(word, text):
	return 100*([word for word in text ].count(word))/len(text)

fdist4 = nltk.FreqDist([word.lower() for word in text4 if word.isalpha()])
vocabulary4_tuples = fdist4.items()
vocabulary4_tuples = sorted(vocabulary4_tuples, key = lambda vocab: vocab[1], reverse = True) 

percent = 0
words = []

for i in range(len(vocabulary4_tuples)):
	if percent <= 33:
		words.append(vocabulary4_tuples[i][0])
		percent += percentage(vocabulary4_tuples[0], text4)

print words