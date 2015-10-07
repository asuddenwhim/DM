from nltk import word_tokenize, sent_tokenize
text = "Generally, data mining (sometimes called data or knowledge discovery) is the process of analyzing data from different perspectives and summarizing it into useful information - information that can be used to increase revenue, cuts costs, or both. Data mining software is one of a number of analytical tools for analyzing data. It allows users to analyze data from many different dimensions or angles, categorize it, and summarize the relationships identified. Technically, data mining is the process of finding correlations or patterns among dozens of fields in large relational databases. "
sents = sent_tokenize(text)
tokens = word_tokenize(text)
textObj = Text(tokens)
print len(sents)
print len(tokens)
print textObj
