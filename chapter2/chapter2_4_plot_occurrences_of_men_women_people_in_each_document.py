cfd = nltk.ConditionalFreqDist((target, fileid[:4]) for fileid in state_union.fileids() 
	for w in state_union.words(fileid) for target in ['women', 'men', 'people'] if w.lower().startswith(target))

cfd.plot()