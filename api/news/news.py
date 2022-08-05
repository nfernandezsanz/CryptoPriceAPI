
import re
import os
import pyshorteners
from newsapi    import NewsApiClient
from datetime   import datetime, timedelta
from newspaper  import Article
from newspaper  import Config

api_key   = os.getenv('NEWS_API')
type_tiny = pyshorteners.Shortener()

def get_news(crypto, max = 10):

    newsapi = NewsApiClient(api_key=os.getenv('NEWS_API', ''))
    d_from  = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')

    headlines = newsapi.get_everything(
        q=crypto.name,
        language="en",
        page_size=100,
        sort_by="relevancy",
        from_param=d_from,
    )

    articulos_ = headlines['articles']

    articulos  = list()

    for articulo in articulos_:
        if( crypto.name.lower() in articulo['title'].lower()):
            articulos.append(articulo)
        if( len(articulos) >= max):
            break

    if(len(articulos) <= 0):
        print("Problemon... no encontre articulos...")
        articulos = articulos_[:max]

    # Extraigo todo el texto...
    for articulo in articulos:
        
        article = Article(articulo['url'])

        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        config = Config()
        config.browser_user_agent = user_agent

        try:
            article.download()
            article.parse()
            content = article.text

            content = content.lower()
            content = re.sub(r"[^a-zA-Z0-9]+", ' ', content)

            articulo['contnet'] = content
        except:
            pass

    return articulos