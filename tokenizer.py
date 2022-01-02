from nltk import word_tokenize

def tokenizer(content):
    token_words = word_tokenize(content)
    
    return token_words