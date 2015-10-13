import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer 

sample_text = state_union.raw("2006-GWBush.txt")
train_text = state_union.raw("2005-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(sample_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

# def process_content():
# 	try:
# 		for i in tokenized:
# 			words = nltk.word_tokenize(i)
# 			tags = nltk.pos_tag(words)

# 			print(tags)
# 	except:
# 		print 'fail'

# process_content()

