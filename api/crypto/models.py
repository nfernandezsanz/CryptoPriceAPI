from django.db        import models
from .coingecko       import get_price
from django.db.models import Avg

class Crypto(models.Model):
    name        = models.CharField(max_length=80, unique=True)
    symbol      = models.CharField(max_length=80)

    @property
    def price_now(self):
        price = get_price(self.name, self.symbol)
        return price

    def __str__(self):
        return self.name + f" ({self.symbol.upper()})"
    class Meta:
        ordering = ['name']
        
class PriceRecord(models.Model):
    crypto     = models.ForeignKey(Crypto, on_delete=models.CASCADE, default=None)
    timestamp  = models.DateTimeField(auto_now_add=True)
    price      = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.crypto.symbol.upper()} ({self.timestamp.date()}) --> {round(self.price,2)}USD"
    class Meta:
        ordering = ['timestamp']

