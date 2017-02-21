import nltk
import relations

tokenizer = nltk.tokenize.punkt.PunktSentenceTokenizer()
wordnet_lemmatizer = nltk.stem.WordNetLemmatizer()
punkt_word_tokenizer = nltk.tokenize.WordPunctTokenizer()

def get_relations(text,ner_tags,lang_tag):
    all_relations = {}
    if lang_tag == 'en':
        sentences = tokenizer.tokenize(text)
        relationships = set([wordnet_lemmatizer.lemmatize(i.lower()) for i in relations.relations])
        for sentence in sentences:
            tokenized_sentence = punkt_word_tokenizer.tokenize(sentence)
            lemmatized_sentence = [wordnet_lemmatizer.lemmatize(token.lower()) for token in tokenized_sentence]
            a,b,r = '','',''
            for word in lemmatized_sentence:
                if word in relationships:
                    r = word
                elif word in ner_tags:
                    if a == '':
                        a = word
                    else:
                        b = word
            if (a!='') or (b!='') or (r!=''):
                print(lemmatized_sentence)
                print((a,b,r))
            if (((a != '') and (b!='')) and (r!='')):
                if (a,b,r) in all_relations:
                    all_relations[(a,b,r)] = all_relations[(a,b,r)]+1
                else:
                    all_relations[(a,b,r)] = 1
    return all_relations
                    
            
            
