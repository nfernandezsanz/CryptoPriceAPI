from GoogleNews import GoogleNews

googlenews = GoogleNews()
googlenews = GoogleNews(lang='en', region='US')
googlenews = GoogleNews(period='1d')

#googlenews = GoogleNews(start='02/01/2020',end='02/28/2020')


print("GET")

googlenews.get_news('BTC')

print(googlenews.results()[0]['title'])