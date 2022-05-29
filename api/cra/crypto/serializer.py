from rest_framework import serializers
from .models import Crypto, PriceRecord, Sentiment


class CryptoSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Crypto
        fields = '__all__'

class PriceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model  = PriceRecord
        fields = '__all__'

class SentimentSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Sentiment
        fields = '__all__'
    
    def to_representation(self, instance):
        representation          = super().to_representation(instance)

        representation['crypto']= instance.crypto.name

        representation['price'] = str(instance.price.price) + " USD"
 
        if(instance.sentiment == 0):
            representation['sentiment']= "NEUTRAL"
        elif(instance.sentiment > 0):
            representation['sentiment']= "POSITIVE"
        else:
            representation['sentiment']= "NEGATIVE"

        representation['rta']          = round(instance.sentiment,2)

        representation['sources']      = instance.source

        return representation