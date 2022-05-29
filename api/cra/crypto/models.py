from django.db  import models
from .coingecko import get_price
import os


class Crypto(models.Model):
    name        = models.CharField(max_length=80)
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
