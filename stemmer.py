from nltk.stem import PorterStemmer
porter = PorterStemmer()

def stemmer(token_words):
    stem_sentence=[]
    for word in token_words:
        stem_sentence.append(porter.stem(word))
        stem_sentence.append(" ")
    return "".join(stem_sentence)
