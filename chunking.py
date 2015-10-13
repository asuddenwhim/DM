import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer 
from nltk.chunk import RegexpParser

sample_text = state_union.raw("2006-GWBush.txt")
train_text = state_union.raw("2005-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(sample_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
	try:
		for i in tokenized:
			words = nltk.word_tokenize(i)
			tags = nltk.pos_tag(words)
			#look for adverbs
			#chunk grammar
			chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP><NN>?}"""
			print 'reg'
			#chunk parser
			chunkParser = nltk.RegexpParser(chunkGram)
			print 'regp'
			chunked = chunkParser.parse(tags)

			chunked.draw()
			
	except Exception as e:
		print e

process_content()
