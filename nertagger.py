# -*- coding: utf-8 -*-

from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

def ner_tag(text):
    st = StanfordNERTagger('/home/nurendra/Downloads/stanford/english.all.3class.nodistsim.crf.ser.gz',
					   '/home/nurendra/Downloads/stanford/stanford-ner-2016-10-31/stanford-ner.jar',
					   encoding='utf-8')

    # e.g text = 'While in France, Christine Lagarde discussed short-term stimulus efforts in a recent interview with the Wall Street Journal.'
    tokenized_text = word_tokenize(text)
    classified_text = st.tag(tokenized_text)
    names = []
    for i in classified_text:
        if i[1] == 'PERSON':
            names.append(i[0].lower())
    return names
    # return form: [('While', 'O'), ('in', 'O'), ('France', 'LOCATION'), (',', 'O'), ('Christine', 'PERSON'), ('Lagarde', 'PERSON'), ('discussed', 'O'), ('short-term', 'O'), ('stimulus', 'O'), ('efforts', 'O'), ('in', 'O'), ('a', 'O'), ('recent', 'O'), ('interview', 'O'), ('with', 'O'), ('the', 'O'), ('Wall', 'ORGANIZATION'), ('Street', 'ORGANIZATION'), ('Journal', 'ORGANIZATION'), ('.', 'O')]


