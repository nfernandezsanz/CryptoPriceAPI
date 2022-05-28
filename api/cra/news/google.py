
import re
import os
import spacy
import requests
import pyshorteners
from GoogleNews import GoogleNews
from newsapi    import NewsApiClient
from bs4        import BeautifulSoup
from datetime   import datetime, timedelta

api_key   = os.getenv('NEWS_API')
type_tiny = pyshorteners.Shortener()
#googlenews = GoogleNews(start='02/01/2020',end='02/28/2020')

def get_news_google(crypto, max = 10):

    googlenews = GoogleNews()
    googlenews = GoogleNews(lang='en', region='US')
    googlenews = GoogleNews(period='1d')

    googlenews.set_encode('utf-8')

    googlenews.get_news(crypto)

    articles = googlenews.results()[:max]


    post_list = []
    for article in articles:
        short_url = type_tiny.tinyurl.short("http://"+ article['link'])
        post = {"crypto":crypto,"title":article['title'], "source":article['site'], "link":short_url}
        post_list.append(post)

    googlenews.clear()
    return post_list


def get_news(crypto, max = 10):

    newsapi = NewsApiClient(api_key="a32c4d1be7704492ae764375eb5436d6")
    d_from  = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')

    headlines = newsapi.get_everything(
        q=crypto.name,
        language="en",
        page_size=100,
        sort_by="relevancy",
        from_param=d_from,
    )

    articulos = headlines['articles'][:max]

    return articulos
