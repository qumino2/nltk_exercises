import nltk
from nltk.corpus import brown

cfd = nltk.ConditionalFreqDist((genre, word) for genre in brown.categories() 
	for word in brown.words(genre = categories ))
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

cfd.plot(samples = days )