from .models                    import Crypto, PriceRecord
from .serializer                import CryptoSerializer, PriceRecordSerializer
from rest_framework             import viewsets, status, permissions
from rest_framework.response    import Response
from rest_framework.decorators  import action
from rest_framework             import viewsets, status, permissions
from .coingecko                 import get_cryptos

def load_cryptos():
    print("Downloading cryptos...")
    list    = get_cryptos()
    print(f"Downloadead {len(list)} cryptos")
    cryptos = Crypto.objects.all().values_list('name', flat=True)
    print("Loading cryptos..")
    for c in list:
        #Protejo que no se repitan los datos
        if(c['name'] not in cryptos):
            try:
                n = Crypto()
                n.name   = c['name']
                n.symbol = c['symbol'] 
                n.save()
            except:
                pass
    print("Cryptos loaded")
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