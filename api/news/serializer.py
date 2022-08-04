from rest_framework import serializers
from crypto.models import Opinion, Analisis, Source


class OpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Opinion
        fields = '__all__'
    
    def to_representation(self, instance):
        representation           = super().to_representation(instance)
        representation['crypto'] = instance.crypto.name

        representation['source'] = instance.source.name
 
        if(instance.analisis.sentiment == 0):
            representation['sentiment']= "NEUTRAL"
        elif(instance.analisis.sentiment > 0):
            representation['sentiment']= "POSITIVE"
        else:
            representation['sentiment']= "NEGATIVE"
        
        representation['analisis']     = round(instance.analisis.sentiment,2)
        representation['MFwords']      = instance.analisis.fre
        representation['NERs']         = instance.analisis.ners

        return representation




class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Source
        fields = '__all__'
    
    def to_representation(self, instance):
        representation            = super().to_representation(instance)

        if(instance.afinity == 0):
            representation['afinity'] = "NEUTRAL"
        elif(instance.afinity < 0):
            representation['afinity'] = "ANTI-CRYPTO"
        else:
            representation['afinity'] = "CRYPTO AMIGO"

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
        try:
            representation['article']      = Opinion.objects.filter(analisis=instance).last().link
        except:
            representation['article']      = "Link not found"
        return representation