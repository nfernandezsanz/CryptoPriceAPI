from rest_framework import serializers
from .models import Opinion, Analisis, Source


class OpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Opinion
        fields = '__all__'
    
    def to_representation(self, instance):
        representation           = super().to_representation(instance)
        representation['crypto'] = instance.crypto.name

        representation['source'] = instance.source.name
 
        if(instance.sentiment == 0):
            representation['sentiment']= "NEUTRAL"
        elif(instance.sentiment > 0):
            representation['sentiment']= "POSITIVE"
        else:
            representation['sentiment']= "NEGATIVE"

        return representation
class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Source
        fields = '__all__'
    
    def to_representation(self, instance):
        representation           = super().to_representation(instance)
        representation['afinity'] = instance.afinity
        return representation
class AnalisisSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Analisis
        fields = '__all__'
    
    def to_representation(self, instance):
        representation           = super().to_representation(instance)
        representation['rta']    = instance.sentiment

        if(instance.sentiment == 0):
            representation['sentiment']= "NEUTRAL"
        elif(instance.sentiment > 0):
            representation['sentiment']= "POSITIVE"
        else:
            representation['sentiment']= "NEGATIVE"

        return representation