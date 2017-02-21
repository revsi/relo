#!/usr/bin/python3
# Research Center : LTRC, IIIT Hyderabad
__author__ = ["Akirato","revsi"]

import sys,codecs,re
import nertagger
import postagger
import nltk
import pickle
import relo

debug = True
punkt_word_tokenizer = nltk.tokenize.WordPunctTokenizer()

def main():
    if len(sys.argv)<2:
        print("Please give the input file as argument.")
        return None
    with codecs.open(sys.argv[1], 'r', encoding='utf-8') as myfile:
        text=myfile.read()
    print("============================RELO============================")
    print("Input Story : ",text)
    print("=======================Making the NER model==================\n\n")
    tokenized_text = punkt_word_tokenizer.tokenize(text)
    ner_tags = set(nertagger.ner_tag(' '.join(tokenized_text)))
    ner_file = open(sys.argv[1]+'.ner','wb')
    pickle.dump(ner_tags,ner_file)
    ner_file.close()
    ner_file = open(sys.argv[1]+'.ner','rb')
    ner_tags = pickle.load(ner_file)
    ner_file.close()
    print(ner_tags) 
    print("===========================Results===========================\n\n")
    relations = relo.get_relations(text,ner_tags,lang_tag='en')
    print(relations)

if __name__ == "__main__":
    main()
