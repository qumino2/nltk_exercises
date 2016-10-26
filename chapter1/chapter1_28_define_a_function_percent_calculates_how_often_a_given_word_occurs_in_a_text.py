def percent(word, text):
	return str(100*len([w for w in text if w.lower() == word.lower()])/len(text)) + '%' 