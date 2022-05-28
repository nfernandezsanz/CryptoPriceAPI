from pycoingecko import CoinGeckoAPI


def get_price(name , symbol):
    price = 0
    try:
        cg    = CoinGeckoAPI()
        name  = name.lower()
        rta   = cg.get_price(ids=name, vs_currencies='usd')
        price = rta[name]['usd']
    except:
        pass

    return price


