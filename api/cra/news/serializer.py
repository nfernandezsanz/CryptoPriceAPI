from rest_framework import serializers
from .models import Opinion, Analisis


class OpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Opinion
        fields = '__all__'

class AnalisisSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Analisis
        fields = '__all__'

