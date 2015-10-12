from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_words = ['python', 'pythoner', 'pythonning', 'pythoned', 'pythonly']

for w in example_words:
	print ps.stem(w)