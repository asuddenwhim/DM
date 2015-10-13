import nltk
# from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer 
from nltk.chunk import RegexpParser

sample_text = "Samsung's galaxy Note 5 is excellent overall, and the only phone to buy if you want to write by hand. However, you'll pay a huge premium for a modest upgrade from last year's model, and less pricey competitors will satisfy many."
train_text = "Samsung has packed in more power, an even better display and a great camera making the Note 4 for an excellent smartphone. It'll be too big for some and the S Pen is still questionable, but overlook this and you'll be happy."

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
	try:
		for i in tokenized:
			words = nltk.word_tokenize(i)
			tags = nltk.pos_tag(words)
			namedEnt = nltk.ne_chunk(tags)
			namedEnt.draw()
	except Exception as e:
		print e

process_content()
