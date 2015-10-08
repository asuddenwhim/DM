from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = "Generally, data mining (sometimes called data or knowledge discovery) is the process of analyzing data from different perspectives and summarizing it into useful information - information that can be used to increase revenue, cuts costs, or both. Data mining software is one of a number of analytical tools for analyzing data. It allows users to analyze data from many different dimensions or angles, categorize it, and summarize the relationships identified. Technically, data mining is the process of finding correlations or patterns among dozens of fields in large relational databases. "
stop_words = set(stopwords.words("english"))

words = word_tokenize(text)

filtered_sentence = []

for w in words:
	if w not in stop_words:
		filtered_sentence.append((w))

print filtered_sentence
