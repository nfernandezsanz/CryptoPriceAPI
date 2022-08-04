from crypto.models              import Opinion, Analisis, Source
from .serializer                import OpinionSerializer, AnalisisSerializer, SourceSerializer
from rest_framework             import viewsets, status, permissions
from rest_framework.response    import Response
from rest_framework.decorators  import action
from datetime                   import datetime, timedelta
from rest_framework             import viewsets, status, permissions



class NewsViewSet(viewsets.ModelViewSet):
    serializer_class   = OpinionSerializer
    queryset           = Opinion.objects.all()


class AnalisisViewSet(viewsets.ModelViewSet):
    serializer_class   = AnalisisSerializer
    queryset           = Analisis.objects.all()


class SourceViewSet(viewsets.ModelViewSet):
    serializer_class   = SourceSerializer
    queryset           = Source.objects.all()
