from django.contrib import admin
from .models import Sentiment, Source , Opinion, Analisis

# Register your models here.

class AnalisisAdmin(admin.StackedInline):
    model = Analisis

class Opiniones(admin.StackedInline):
    model = Opinion
    inlines = [AnalisisAdmin]

@admin.register(Sentiment)
class SentimentAdmin(admin.ModelAdmin):
    list_display = ('crypto', 'timestamp', 'sentiment')
    inlines = [Opiniones]
    search_fields = ['crypto',]
    list_filter = ('sentiment', )
    

@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('name','afinity_str')
    search_fields = ['name', 'afinity_str']
    #list_filter = ('afinity_str', )

