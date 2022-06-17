import sklearn
import numpy as np
import matplotlib as plt


from sklearn.feature_extraction.text import CountVectorizer
import nltk.stem
import nltk

stopword_es     = nltk.corpus.stopwords.words('spanish')
spanish_stemmer = nltk.stem.SnowballStemmer('spanish')

class StemmedCountVectorizer_ES(CountVectorizer):
    def build_analyzer(self):
        analyzer = super(StemmedCountVectorizer_ES, self).build_analyzer()
        return lambda doc: (spanish_stemmer.stem(w) for w in analyzer(doc))

stem_vectorizer_ES = StemmedCountVectorizer_ES(stop_words=stopword_es)

stem_analyze_ES = stem_vectorizer_ES.build_analyzer()


Y = stem_analyze_ES("Lucas leyo todo el torá y le dio dolor de tórax")

X = stem_analyze_ES("Johny compro zanahorias y papas")

for tok in Y:
    print(tok)

for tok in X:
    print(tok)

nltk.download('cess_esp')
from nltk.corpus import cess_esp as cess
print(cess.words()[:10])