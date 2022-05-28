from django.urls    import path, include
from rest_framework import routers
from .              import viewsets

app_name = "Crypto"

router = routers.DefaultRouter(trailing_slash=False)

router.register('cypto'     , viewsets.CryptoViewSet)

router.register('price'     , viewsets.PriceRecordViewSet)

router.register('sentiment' , viewsets.SentimentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]