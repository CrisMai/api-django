from dataclasses import field
from rest_framework import serializers
from .models import Conta
from .models import Extrato

class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        fields = '__all__'

class ExtratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extrato
        fields = '__all__'
     