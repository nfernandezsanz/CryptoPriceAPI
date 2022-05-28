from .models                    import Crypto, PriceRecord, Sentiment
from .serializer                import CryptoSerializer, PriceRecordSerializer, SentimentSerializer
from rest_framework             import viewsets, status, permissions
from rest_framework.response    import Response
from rest_framework.decorators  import action
from rest_framework             import viewsets, status, permissions

from datetime                   import datetime, timedelta
from django.utils               import timezone        
from django.utils.timezone      import make_aware
from news.google                import get_news
from news.sentiment             import analize


class CryptoViewSet(viewsets.ModelViewSet):
    serializer_class   = CryptoSerializer
    queryset           = Crypto.objects.all()


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

class SentimentViewSet(viewsets.ModelViewSet):
    serializer_class   = SentimentSerializer
    queryset           = Sentiment.objects.all()


    @action(detail=False, methods=['get',])
    def historic(self,request,pk=None):
        crypto    = request.query_params.get('crypto', None)

        if(not crypto):
            return Response({"msg": "Ingrese una crypto", "error_code": "400"}, 
                             status=status.HTTP_400_BAD_REQUEST)  
        
        crypto = Crypto.objects.filter(name = crypto).last()

        if(not crypto):
            return Response({"msg": "Crypto not suported", "error_code": "400"}, 
                             status=status.HTTP_400_BAD_REQUEST)  
        
        date_from = request.query_params.get('from'  , None)

        if date_from:
            date_from = make_aware(datetime.strptime(date_from, '%d/%m/%Y'))
        else:
            date_from = timezone.now() - timedelta(days=7)

        date_to = request.query_params.get('to', None)
        
        if date_to:
            date_to = make_aware(datetime.strptime(date_to, '%d/%m/%Y'))
        else:
            date_to = timezone.now()

        if(date_to - date_from < timedelta(days=1)):
            return Response({"msg": "Fechas incongruentes", "error_code": "400"}, 
                                status=status.HTTP_400_BAD_REQUEST)  


        sentiments = Sentiment.objects.filter(timestamp__range=[date_from, date_to], crypto=crypto)

        rta = {}

        rta['date_from']  = date_from
        rta['date_to']    = date_to
        rta['sentiments'] = SentimentSerializer(sentiments, many=True).data
        rta['count']      = sentiments.count()

        return Response(rta)
    
    @action(detail=False, methods=['get',])
    def now(self,request,pk=None):
        crypto    = request.query_params.get('crypto', None)

        if(not crypto):
            return Response({"msg": "Ingrese una crypto", "error_code": "400"}, 
                             status=status.HTTP_400_BAD_REQUEST)  
        
        crypto = Crypto.objects.filter(name = crypto).last()

        if(not crypto):
            return Response({"msg": "Crypto not suported", "error_code": "400"}, 
                             status=status.HTTP_400_BAD_REQUEST)  

        # Me traigo el precio.. y de paso lo guardo
        price = crypto.price_now
        
        # Me traigo las noticias
        news = get_news(crypto)

        sum  = 0

        for new in news:
            rta = analize(new, crypto)
            sum += rta

        rta = Sentiment()
        rta.crypto    = crypto
        rta.sentiment = sum
        rta.price     = #Falta esto

        rta.save()

        return Response("Funny")