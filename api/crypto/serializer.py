from rest_framework import serializers
from .models import Crypto, PriceRecord


class CryptoSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Crypto
        fields = '__all__'

class PriceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model  = PriceRecord
        fields = '__all__'

