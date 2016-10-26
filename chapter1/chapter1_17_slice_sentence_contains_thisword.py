import nltk

from nltk.book import *

for  var in [i for i, j in enumerate(text9) if j == 'sunset']:
	ori_var = var
	pun = ['.', '!', '?']
	stop = 0 
	start = 0
	while stop == 0 or start == 0:
		if text9[var] not in pun  and stop == 0:
			var += 1

		elif text9[var] in pun  and stop == 0:
			stop = var + 1
			var = ori_var

		elif text9[var] not in pun and stop != 0 :
			var -= 1

		elif text9[var] in pun and stop != 0:
			start = var + 1

	print "start from %d end in %d" % (start, stop)
	print ' '.join(text9[start:stop])