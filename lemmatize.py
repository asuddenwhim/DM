from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print (lemmatizer.lemmatize('deliberately'))
print (lemmatizer.lemmatize('prettier', pos='a'))
print (lemmatizer.lemmatize('better', pos='a'))