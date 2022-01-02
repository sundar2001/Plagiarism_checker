import nltk
import colorama
from colored import fg
from read_files import *
from convert_to_lowercase import *
from remove_stopwords import *
from remove_punctuation import *
from tokenizer import *
from stemmer import *
from calculate_similarity import similarity

#colors
blue  = fg('blue')
green = fg('green')
red   = fg('red')
black = fg('black')


#read files content
f_content1, f_content2 = readFiles()
print(" ")
print(blue + ">>>>>>>>>>>>>>>>>>>>FILE CONTENT<<<<<<<<<<<<<<<<<<<<<")
print(red + "#file1: ")
print(black + f_content1)
print(" ")
print(red + "#file2: ")
print(black + f_content2)
print(" ")

#convert the files content into lowercase
l_content1, l_content2 = convertToLowercase(f_content1, f_content2)
print(" ")
print(blue + ">>>>>>>>>>>>>>>>>>>LOWERCASE CONVERSION<<<<<<<<<<<<<<<<<<<")
print(red + "#file1: ")
print(black + l_content1)
print(" ")
print(red + "#file2: ")
print(black + l_content2)
print(" ")

#removing stop words like ["i", "me", "my", ..]
rs_content1, rs_content2 = removeStopwords(l_content1, l_content2)
print(" ")
print(blue + ">>>>>>>>>>>>>>>>>AFTER REMOVING STOP WORDS<<<<<<<<<<<<<<<<")
print(red + "#file1: ")
print(black + rs_content1)
print(" ")
print(red + "#file2: ")
print(black + rs_content2)

#removing punctuations (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)
c_content1, c_content2 = removePunctuation(rs_content1, rs_content2)
print(" ")
print(blue + ">>>>>>>>>>>>>>>>>AFTER REMOVING PUNCTUATION<<<<<<<<<<<<<<<<")
print(red + "#file1: ")
print(black + c_content1)
print(" ")
print(red + "#file2: ")
print(black + c_content2)

#tokenize
tokenized_words1 = tokenizer(c_content1)
tokenized_words2 = tokenizer(c_content2)
print(" ")
print(blue + ">>>>>>>>>>>>>>>>>AFTER TOKENIZATION<<<<<<<<<<<<<<<<")
print(red + "#file1: ")
print(black + " ")
print(tokenized_words1)
print(" ")
print(red + "#file2: ")
print(black + " ")
print(tokenized_words2)


#stemming
stemmed_words1 = stemmer(tokenized_words1)
stemmed_words2 = stemmer(tokenized_words2)
print(" ")
print(blue + ">>>>>>>>>>>>>>>>>AFTER STEMMING<<<<<<<<<<<<<<<<")
print(red + "#file1: ")
print(black + stemmed_words1)
print(" ")
print(red + "#file2: ")
print(black + stemmed_words2)

#display similarity
similarity_ = similarity(stemmed_words1, stemmed_words2)
print(" ")
print(" ")
print(black + "-----------------------------------------------------------")
print(green + "SIMILARITY: ", similarity_, "%")
print(black + "-----------------------------------------------------------")