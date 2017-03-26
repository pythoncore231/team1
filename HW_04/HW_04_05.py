"""The set text display all words beginning with a sequence
symbols."""
text = " compare adsafss afadsfasfas sdggdsgds dsgdsgd " + "compare " * 10
for word in text.split():
	if "com" in word and "a" in word:
		print word


text = 'abv 111'
print text.split('a')
print dir(str)

