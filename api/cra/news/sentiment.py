
import re
import spacy
import requests
from bs4                  import BeautifulSoup
from collections          import Counter
from nltk.tokenize        import word_tokenize
from nltk.corpus          import stopwords
from nltk.stem            import WordNetLemmatizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from .models              import Opinion,Analisis

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

def post_content(link):

    headers  = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    res      = requests.get(link, headers=headers)
    soup     = BeautifulSoup(res.content, "html.parser")
    content  = soup.get_text()
    content  = re.sub('https:\/\/\S+', '', content)
    content  = re.sub("\n","",content)
    content  = re.sub("\t","",content)
    return content.lower()

def analize_sentiment(content, debug = False):
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

def analize(posteo, debug = False):
    
    op        = Opinion()
    op.crypto = posteo['crypto']
    op.source = posteo['source']
    op.link   = posteo['link']

    content = post_content(posteo['link'])
    
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

    return op
