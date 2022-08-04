from django.contrib import admin
from .models import Crypto, PriceRecord 
@admin.register(Crypto)
class CryptoAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol')
    search_fields = ['name', 'symbol']

@admin.register(PriceRecord)
class PriceRecordAdmin(admin.ModelAdmin):
    list_display = ('crypto', 'timestamp', 'price')
    search_fields = ['crypto', 'timestamp']
