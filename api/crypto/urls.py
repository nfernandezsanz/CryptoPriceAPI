from django.urls    import path, include
from rest_framework import routers
from .              import viewsets

app_name = "Crypto"

router = routers.DefaultRouter(trailing_slash=False)

router.register('crypto'     , viewsets.CryptoViewSet)

router.register('price'     , viewsets.PriceRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]