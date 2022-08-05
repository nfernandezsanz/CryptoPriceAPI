from .models                    import Crypto, PriceRecord
from .serializer                import CryptoSerializer, PriceRecordSerializer
from rest_framework             import viewsets, status, permissions
from rest_framework.response    import Response
from rest_framework.decorators  import action
from rest_framework             import viewsets, status, permissions
from .coingecko                 import get_cryptos


prohibit = ['x', '/', 'BTC', 'ADA', 'DAO', '$' , '-', '+', 'up', 'down', ' ', '.', '#']
def str__(int):
    return str(int)
prohibit.extend(list(map(str__,range(11))))

def load_cryptos():
    print("Downloading cryptos...")
    list    = get_cryptos()
    print(f"Downloadead {len(list)} cryptos")
    cryptos = Crypto.objects.all().values_list('name', flat=True)
    print("Loading cryptos..")
    count = 0
    for c in list:
        #Protejo que no se repitan los datos
        name = c['name'].lower()
        symbol = c['symbol'].lower()

        if(any(ext in name for ext in prohibit)):
            continue

        if(name not in cryptos):
            try:
                n = Crypto()
                n.name   = name
                prohibit.append(name)
                n.symbol = symbol
                n.save()
                count += 1
            except:
                pass

    print(f"Cryptos loaded {count} cryptos!")
class CryptoViewSet(viewsets.ModelViewSet):
    serializer_class   = CryptoSerializer
    queryset           = Crypto.objects.all()

    @action(detail=False, methods=['get', 'post'])
    def download(self,request,pk=None):
        load_cryptos()
        return Response(CryptoSerializer(Crypto.objects.all(), many=True).data)

class PriceRecordViewSet(viewsets.ModelViewSet):
    serializer_class   = PriceRecordSerializer
    queryset           = PriceRecord.objects.all()

    @action(detail=False, methods=['get', 'post'])
    def priceRegister(self,request,pk=None):
        cr = Crypto.objects.all()
        d = list()
        for c in cr:
            d.append({c.name:c.price_now})
        return Response(d)