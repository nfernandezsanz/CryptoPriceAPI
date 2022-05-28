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