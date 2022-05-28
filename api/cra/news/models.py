from django.db     import models
from crypto.models import Crypto, PriceRecord

class Analisis(models.Model):
    ners       = models.TextField()
    fre        = models.TextField()
    sentiment  = models.FloatField(default=0)

# Create your models here.
class Opinion(models.Model):
    crypto     = models.ForeignKey(Crypto, on_delete=models.CASCADE, default=None)
    timestamp  = models.DateTimeField(auto_now_add=True)
    source     = models.CharField(max_length=128, blank=False)
    link       = models.URLField()
    analisis   = models.ForeignKey(Analisis, on_delete=models.CASCADE)






    