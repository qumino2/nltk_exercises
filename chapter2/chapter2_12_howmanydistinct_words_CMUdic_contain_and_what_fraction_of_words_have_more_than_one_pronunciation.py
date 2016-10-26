from nltk.corpus import cmudict as cmu
entries = cmu.entries()
words = 0
multiples = 0

for i in range(0, len(entries)):
	if entries[i-1][1] != entries[i][1]:
		words += 1
	elif entries[i-1] != entries[i-2]:
		multiples += 1

print 'Words:' + str(words)
print 'multiples:' + str(multiples)
print 'Fraction:' + str(multiples/ words)
