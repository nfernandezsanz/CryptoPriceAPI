from GoogleNews import GoogleNews
from .sentiment import analisis_sentiment

#googlenews = GoogleNews(start='02/01/2020',end='02/28/2020')

def get_news(crypto, max = 10):

    googlenews = GoogleNews()
    googlenews = GoogleNews(lang='en', region='US')
    googlenews = GoogleNews(period='1d')

    googlenews.set_encode('utf-8')

    googlenews.get_news(crypto)

    articles = googlenews.results()[:max]

    for article in articles:
        post = {"title":article['title'], "source":article['site'], "link":article['link']}
        analisis_sentiment(post)

    #print(googlenews.get_texts())
    #print(googlenews.get_links())
    

    googlenews.clear()
get_news("bitcoin")