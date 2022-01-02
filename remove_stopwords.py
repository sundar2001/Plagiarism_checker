from nltk.corpus import stopwords
sw_nltk = stopwords.words('english')

def removeStopwords(l_content1, l_content2):
    words_1 = [word for word in l_content1.split() if word not in sw_nltk]
    removed_stopwords_1 = " ".join(words_1)
    words_2 = [word for word in l_content2.split() if word not in sw_nltk]
    removed_stopwords_2 = " ".join(words_2)

    return removed_stopwords_1, removed_stopwords_2