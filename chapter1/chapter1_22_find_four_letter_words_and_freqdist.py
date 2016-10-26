fdist5 = nltk.FreqDist([word.lower() for word in text5 if word.isalpha() and len(word) ==4])

vocabulary5_tuples = fdist5.items()

vocabulary5_tuples = sorted(vocabulary5_tuples, key = lambda  v: v[1])

vocabulary5 = []

for item in vocabulary5_tuples:
	vocabulary5.insert(0, item[0])

print vocabulary5