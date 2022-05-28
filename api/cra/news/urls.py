from django.urls    import path, include
from rest_framework import routers
from .              import viewsets

app_name = "news"

router = routers.DefaultRouter(trailing_slash=False)

router.register('news'       , viewsets.NewsViewSet)
router.register('analisis'   , viewsets.AnalisisViewSet)

urlpatterns = [
    path('', include(router.urls)),
]