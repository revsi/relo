#!/usr/bin/python3
# Research Center : LTRC, IIIT Hyderabad
__author__ = ["Akirato","revsi"]

import sys,codecs,re
from string import punctuation
import nertagger
import postagger
import nltk
debug = True
r = re.compile(r'[\s{}]+'.format(re.escape(punctuation)))
print(dir(nltk.tokenize))
punkt_word_tokenizer = nltk.tokenize.WordPunctTokenizer()

def main():
    if len(sys.argv)<2:
        print("Please give the input file as argument.")
        return None
    with codecs.open(sys.argv[1], 'r', encoding='utf-8') as myfile:
        text=myfile.read()
    print("============================RELO============================")
    print("Input Story : ",text)
    print("===========================Results===========================\n\n")
    ner_tags = set(nertagger.ner_tag(' '.join(punkt_word_tokenizer.tokenize(text))))
    print(ner_tags)
#        print(pos_tags)    
        

if __name__ == "__main__":
    main()
