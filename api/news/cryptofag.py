import requests

url = "https://api.alternative.me/fng/?limit=0"

def crypto_fag():
    try:
        response = requests.get(url).json()['data']
        return response[0]['value']
    except:
        return 50

