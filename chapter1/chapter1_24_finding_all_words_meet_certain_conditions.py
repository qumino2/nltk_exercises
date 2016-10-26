#a. Ending in ize
print [word for word in text6 if word.endswith('ize')]
#b. Containing the letter z
print [word for word in text6 if "z" in word]
#c. Containing the sequence of letters pt 
print [word for word in text6 if "pt" in word]
#d. All lowercase letters except for an initial capital (i.e., titlecase)
print [word for word in text6 if word.istitle()]

