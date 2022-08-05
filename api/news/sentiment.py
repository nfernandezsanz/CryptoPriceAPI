
import re
import spacy
from collections          import Counter
from nltk.tokenize        import word_tokenize
from nltk.corpus          import stopwords
from nltk.stem            import WordNetLemmatizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from .models import Opinion,Analisis, Source
import fear_and_greed

analyzer = SentimentIntensityAnalyzer()

def tokenize(content):
    lemmatizer = WordNetLemmatizer()
    sw_addons = {'also', 'since', 'youve'}
    sw = set(stopwords.words('english'))
    regex = re.compile("[^a-zA-Z ]")
    re_clean = regex.sub('', content)

    words = word_tokenize(re_clean)
    lem = [lemmatizer.lemmatize(word) for word in words]
    tokens = [word.lower() for word in lem if word.lower() not in sw.union(sw_addons)]
    return tokens

def token_count(tokens, N=10):
    rta = {}
    for word in Counter(tokens).most_common(N):
        rta[word[0]] = word[1]
    return rta

def analize_sentiment(content):
    sentiment = analyzer.polarity_scores(content)
    return sentiment['compound']

def NERs(content):

    exclude = ['PERCENT', 'MONEY', 'CARDINAL', 'GPE', 'ORDINAL', 'PRODUCT', 'TIME']

    nlp = spacy.load('en_core_web_sm')
    doc = nlp(content)
    
    rta = {}

    labels = []

    for ent in doc.ents:
        if(ent.label_  not in exclude):
            if(ent.label_ not in labels):
                labels.append(ent.label_)
                rta[ent.label_] = []
            rta[ent.label_].append(ent.text)
    for label in labels:
        rta[label] = set(rta[label])
    return rta

def analize(posteo, crypto, sentiment , debug = False):
    
    op           = Opinion()
    op.crypto    = crypto

    source       = Source.objects.filter(name = posteo['source']['name']).last()
    if(not source):
        source      = Source()
        source.name = posteo['source']['name']
        source.save()

    op.source    = source
    op.link      = posteo['url']
    op.sentiment = sentiment
    content      = posteo['content']

    # Sentimiento
    sentiment = analize_sentiment(content)
    ## Analitico
    tokens    = tokenize(content)
    top10     = token_count(tokens)
    ners      = NERs(content)
    #n_grams = Counter(ngrams(tokens, n=3))

    if(debug):
        print()
        print("-----------------------------------SENTIMENT---------------------------------------------")
        if(abs(sentiment) < 0.1):
            print("NEUTRAL")
        elif(sentiment > 0):
            print("POSITIVE")
        else:
            print("NEGATIVE")
        print()
        print("-----------------------------------TOP10---------------------------------------------")
        print()
        print(top10)
        print()
        print("------------------------------------NERs----------------------------------------------")
        print()
        print(ners)
        print()

    an = Analisis()
    an.ners      = str(ners)
    an.fre       = str(top10)
    an.sentiment = sentiment
    
    an.save()
    
    op.analisis = an
    op.save()

    return sentiment
