def  vocab_size(text):
	return len(set([word.lower() for word in text if word.isalpha()]))