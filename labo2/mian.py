import nltk
from nltk.corpus import treebank
from nltk.corpus import brown
from nltk import word_tokenize
import numpy as np

race1 = nltk.tag.str2tuple('race/NN')
race2 = nltk.tag.str2tuple('race/VB')

c_race1 = brown.tagged_words().count(race1)
c_race2 = brown.tagged_words().count(race2)

if(c_race1 > c_race2):
    print("El uso mas frecuente de RACE es como NOUN")
else:
    print("El uso mas frecuente de RACE es como VERB")

unigram_tagger = nltk.tag.UnigramTagger(brown.tagged_sents(categories='news')[:5000])

print("/n-----------------------------------------")
S = "The Secretariat is expected to race tomorrow."
S_tok = word_tokenize(S)
print(unigram_tagger.tag(S_tok))

hmm_tagger = nltk.hmm.HiddenMarkovModelTrainer().train_supervised(brown.tagged_sents(categories="news")[:5000])
print(hmm_tagger.tag(S_tok))

print("/n-----------------------------------------")
R = "The change is possible, if you dont change you die."
R_tok = word_tokenize(R)
print(unigram_tagger.tag(R_tok))
print(hmm_tagger.tag(R_tok))

print("/n-----------------------------------------")
T = "My sister saw bat"
T_tok = word_tokenize(T)
print(unigram_tagger.tag(T_tok))
print(hmm_tagger.tag(T_tok))

print("/n-----------------------------------------")
M = "Juvenile Court to Try Shooting Defendant"
M_tok = word_tokenize(M)
print(hmm_tagger.tag(M_tok))