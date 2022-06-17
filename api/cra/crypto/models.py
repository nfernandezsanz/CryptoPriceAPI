from django.db        import models
from .coingecko       import get_price
from django.db.models import Avg
import os


class Crypto(models.Model):
    name        = models.CharField(max_length=80, unique=True)
    symbol      = models.CharField(max_length=80)

    @property
    def price_now(self):
        price = get_price(self.name, self.symbol)
        return price

    def __str__(self):
        return self.name + f"({self.symbol})"


class PriceRecord(models.Model):
    crypto     = models.ForeignKey(Crypto, on_delete=models.CASCADE, default=None)
    timestamp  = models.DateTimeField(auto_now_add=True)
    price      = models.FloatField(default=0.0)


class Sentiment(models.Model):
    crypto     = models.ForeignKey(Crypto, on_delete=models.CASCADE, default=None)
    timestamp  = models.DateTimeField(auto_now_add=True)
    sentiment  = models.FloatField(default=0.0)
    price      = models.ForeignKey(PriceRecord, on_delete=models.CASCADE, default=None)

    @property
    def source(self):
        try:
            return set(Opinion.objects.filter(sentiment=self).values_list('source__name', flat=True))
        except:
            return []
class Analisis(models.Model):
    ners       = models.TextField()
    fre        = models.TextField()
    sentiment  = models.FloatField(default=0)

class Source(models.Model):
    name = models.CharField(max_length=128, blank=False, unique=True)
    
    @property
    def afinity(self):
        opinions = Opinion.objects.filter(source=self).aggregate(af = Avg('analisis__sentiment'))
        return opinions['af']
    
class Opinion(models.Model):
    crypto     = models.ForeignKey(Crypto, on_delete=models.CASCADE, default=None)
    timestamp  = models.DateTimeField(auto_now_add=True)
    source     = models.ForeignKey(Source, on_delete=models.CASCADE)
    link       = models.TextField()
    analisis   = models.ForeignKey(Analisis, on_delete=models.CASCADE)
    sentiment  = models.ForeignKey(Sentiment, on_delete=models.CASCADE, default=None)