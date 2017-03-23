"""The set text display all words beginning with a sequence
symbols."""
text = "Hello world" * 5
seq = text.find("Hell")
while seq == True:
	print seq
	break