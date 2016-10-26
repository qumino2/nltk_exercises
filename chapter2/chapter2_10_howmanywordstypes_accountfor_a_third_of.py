from __future__ import division
import nltk
from nltk.book import*

def  percentage(word, text):
	return 100 * ([word.lower() for word in text].count(word)/len(text))


fdist5 = nltk.FreqDist([word.lower() for word in text5 if word.isalpha() ])
vocabulary5_tuples = fdist5.items()

vocabulary5_tuples = sorted(vocabulary5_tuples, key = lambda vocab: vocab[1], reverse = True )

percent= 0 
words = []

for i in range(len(vocabulary5_tuples)):
	if percent <= 33:
		words.append(vocabulary5_tuples[i][0])
		percent += percentage(vocabulary5_tuples[i], text5)
	else:
		break

print words



