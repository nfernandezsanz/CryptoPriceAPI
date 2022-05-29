from pycoingecko import CoinGeckoAPI


def get_price(name , symbol):
    price = 0
    try:
        cg    = CoinGeckoAPI()
        name  = name.lower()
        rta   = cg.get_price(ids=name, vs_currencies='usd')
        price = rta[name]['usd']

        print(name, "-->" , price , "USD")
    except:
        pass

    return price


def get_cryptos():
    cg    = CoinGeckoAPI()
    c_list = cg.get_coins_list()
    return c_list

