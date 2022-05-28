from GoogleNews import GoogleNews

#googlenews = GoogleNews(start='02/01/2020',end='02/28/2020')

def get_news(crypto, max = 10):

    googlenews = GoogleNews()
    googlenews = GoogleNews(lang='en', region='US')
    googlenews = GoogleNews(period='1d')

    googlenews.set_encode('utf-8')

    googlenews.get_news(crypto.name)

    articles = googlenews.results()[:max]


    post_list = []
    for article in articles:
        post = {"crypto":crypto,"title":article['title'], "source":article['site'], "link":"http://"+ article['link']}
        post_list.append(post)

    googlenews.clear()
    return post_list
