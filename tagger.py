# from nltk import word_tokenize
import nltk

text = nltk.word_tokenize('The little red riding hood walked through the lovely forest.')
tags = nltk.pos_tag(text)

for w in tags:
	print w[1]