from queue import Empty
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Model
from .models import Conta as ContaModel
from .models import Extrato as ExtratoModel

# Serializers
from .serializers import ContaSerializer
from .serializers import ExtratoSerializer

@api_view(['POST'])
def conta(request):
    serialized_conta= ContaSerializer(data=request.data)
    serialized_conta.is_valid(raise_exception=True)
    serialized_conta.save()
    return Response(serialized_conta.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def contas(request):
    contas = ContaModel.objects.all()
    serialized_contas = ContaSerializer(contas, many=True)
    return Response(serialized_contas.data, status=status.HTTP_200_OK)

    
@api_view(['POST'])
def credito(request):
    serialized_extrato= ExtratoSerializer(data=request.data)
    serialized_extrato.is_valid(raise_exception=True)
    serialized_extrato.save()
    return Response(serialized_extrato.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def debito(request):
    serialized_extrato= ExtratoSerializer(data=request.data)
    serialized_extrato.is_valid(raise_exception=True)
    serialized_extrato.save()
    return Response(serialized_extrato.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def extrato(request, query):
    print("teste1")
    extrato = ExtratoModel.objects.filter(tipo_transacao__icontains=query)
    serialized_extrato = ExtratoSerializer(extrato, many=True)

    if not extrato.exists():
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(serialized_extrato.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def extratoAll(request):
    print("teste2")
    extrato = ExtratoModel.objects.all()
    serialized_extrato = ExtratoSerializer(extrato, many=True)

    return Response(serialized_extrato.data, status=status.HTTP_200_OK)
