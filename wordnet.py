from nltk.corpus import wordnet

#syns = wordnet.synsets('program')

# for i in syns:
# 	print i.lemmas()[0].name()

# for i in syns:
# 	print i.definition()


# for i in syns:
# 	print i.examples()

#generate syn and ant

# synonyms = []
# antonyms = []

# for syn in wordnet.synsets('good'):
# 	for l in syn.lemmas():
# 		synonyms.append(l.name())
# 		if l.antonyms():
# 			antonyms.append(l.antonyms()[0].name())

# print set(synonyms)
# print set(antonyms)

#wup

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('boat.n.01')

print w1.wup_similarity(w2)