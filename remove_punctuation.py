import string

def removePunctuation(content1, content2):
    text_clean_1 = "".join([i for i in content1 if i not in string.punctuation])
    text_clean_2 = "".join([i for i in content2 if i not in string.punctuation])

    return text_clean_1, text_clean_2