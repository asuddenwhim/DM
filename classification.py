import nltk
import random 
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)), category) for category in movie_reviews.categories() for fileid in movie_reviews.fileids(category)]

# documents= []

# for category in movie_reviews.categories():
# 	for fileid in movie_reviews.fileids(category):
# 		documents.append(list(movie_reviews.words(fileid)), category)

random.shuffle(documents)

all_words = []
for w in movie_reviews.words():
	all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)

word_features = list(all_words.keys())[:3000]

def find_features(document):
	words = set(document)
	#features = []
	#boolean
	# for w in word_features:
	# 	features[w] = (w in words) 

	return dict((w, True if w in words else False) for w in word_features)

#print ((find_features(movie_reviews.words('neg/cv000_29416.txt'))))

featuresets = [(find_features(rev),category) for (rev, category) in documents] 

training_set = featuresets[:1900] 
testing_set = featuresets[1900:]

#posterior = prior occurences x likelihood / evidence 

classifier = nltk.NaiveBayesClassifier.train(training_set)

print ('Accuracy %: ', (nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_most_informative_features(15)


