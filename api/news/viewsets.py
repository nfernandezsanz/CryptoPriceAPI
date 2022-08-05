from .models                    import Opinion, Analisis, Source, Sentiment
from crypto.models              import Crypto, PriceRecord
from .serializer                import OpinionSerializer, AnalisisSerializer, SourceSerializer, SentimentSerializer
from rest_framework.response    import Response
from rest_framework.decorators  import action
from datetime                   import datetime, timedelta
from rest_framework             import viewsets, status, permissions
from datetime                   import datetime, timedelta
from django.utils               import timezone        
from django.utils.timezone      import make_aware
from news.news                  import get_news
from news.sentiment             import analize
import fear_and_greed
from .cryptofag import crypto_fag
class NewsViewSet(viewsets.ModelViewSet):
    serializer_class   = OpinionSerializer
    queryset           = Opinion.objects.all()


class AnalisisViewSet(viewsets.ModelViewSet):
    serializer_class   = AnalisisSerializer
    queryset           = Analisis.objects.all()


class SourceViewSet(viewsets.ModelViewSet):
    serializer_class   = SourceSerializer
    queryset           = Source.objects.all()

class SentimentViewSet(viewsets.ModelViewSet):
    serializer_class   = SentimentSerializer
    queryset           = Sentiment.objects.all()


    @action(detail=False, methods=['get',])
    def historic(self,request,pk=None):
        crypto    = request.query_params.get('crypto', None)

        if(not crypto):
            return Response({"msg": "Specify a crypto with the 'crypto' parameter. Example ?crypto=bitcoin", "error_code": "400"}, 
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
            return Response({"msg": "Invalid dates", "error_code": "400"}, 
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
        crypto_    = request.query_params.get('crypto', None)

        if(not crypto_):
            return Response({"msg": "Ingrese una crypto", "error_code": "400"}, 
                             status=status.HTTP_400_BAD_REQUEST)  
        
        crypto = Crypto.objects.filter(name = crypto_).last()

        if(not crypto):
            return Response({"msg": f"Crypto: '{crypto_}' not suported", "error_code": "400"}, 
                             status=status.HTTP_400_BAD_REQUEST)  

        try:
            #Chequeo si no tengo una consulta de hace menos de 30 min
            last_sentiment = Sentiment.objects.filter(crypto=crypto).order_by('timestamp').last()

            if((timezone.now() - last_sentiment.timestamp) < timedelta(minutes=5)):
                return Response(SentimentSerializer(last_sentiment).data)
        except:
            pass


        # Me traigo las noticias
        news = get_news(crypto)

        if(len(news) < 3):
            return Response({"msg": "Not enough articles found", "error_code": "422"}, 
                             status=status.HTTP_422_UNPROCESSABLE_ENTITY)  

        # Me traigo el precio..
        price = crypto.price_now

        # Creo el contenedor final
        sentiment = Sentiment()
        sentiment.crypto = crypto
        
        # Registro el precio actual
        pr    = PriceRecord()
        pr.crypto = crypto
        pr.price  = price
        pr.save() 

        sentiment.price = pr
        sentiment.save()

        # Stocks Fear and greed source 1
        fag1 = float(dict(fear_and_greed.get()._asdict())['value'])
        # Crypto Fear and greed source 2
        fag2 = float(crypto_fag())
        fag = (((fag1 + fag2) / 2.0) - 50 ) / 70 # I divide for the last maximun.. I use it as one extra source
        
        print(f"Fear and greed {fag}")

        sum  = fag
        cant = 1

        for new in news:
            print("\n---------------------------------------------")
            print("\t",new['url'])
            rta = analize(new, crypto, sentiment)
            print("\tResult:", rta)
            sum += rta
            if(rta != 0):
                cant += 1
        
        sum = sum / cant



        sentiment.sentiment = sum
        sentiment.save()

        return Response(SentimentSerializer(sentiment).data)