names=nltk.corpus.names
cfd = nltk.ConditionalFreqDist((fileid, name[0]) for fileid in names.fileids() for name in names.words(fileid))
cfd.plot()