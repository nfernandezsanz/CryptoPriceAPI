from django.db        import models
from crypto.models    import Crypto, PriceRecord
from django.db.models import Avg

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
    link       = models.URLField()
    analisis   = models.ForeignKey(Analisis, on_delete=models.CASCADE)