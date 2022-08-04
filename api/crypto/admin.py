from django.contrib import admin
from .models        import Crypto, PriceRecord, Sentiment, Source , Opinion, Analisis


@admin.register(Crypto)
class CryptoAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol')

@admin.register(PriceRecord)
class PriceRecordAdmin(admin.ModelAdmin):
    list_display = ('crypto', 'timestamp', 'price')


class AnalisisAdmin(admin.StackedInline):
    model = Analisis
class Opiniones(admin.StackedInline):
    model = Opinion
    inlines = [AnalisisAdmin]

@admin.register(Sentiment)
class SentimentAdmin(admin.ModelAdmin):
    list_display = ('crypto', 'timestamp', 'sentiment')
    inlines = [Opiniones]

@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('name','afinity_str')
