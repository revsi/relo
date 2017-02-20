import nltk

def pos_tag(text):
    text = nltk.word_tokenize(text)
    return nltk.pos_tag(text)
