tokens = []
for sent in [sent1, sent2, sent3, sent4, sent5, sent6, sent7, sent8]:
	tokens += sent

sorted(set(word for word in tokens if word.isalpha()))