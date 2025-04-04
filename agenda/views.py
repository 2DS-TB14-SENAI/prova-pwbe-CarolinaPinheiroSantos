from django.shortcuts import render
from . models import Agendamento,Servico
from . serializers import AgendamentoSerializer, ServicoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET'])
def listar_servico(request):
    if request.method == 'GET':
        servico = Servico.objects.all()
        serializer = ServicoSerializer(servico, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])    
def criar_servico(request):
    if request.method == 'POST':
        serializer = ServicoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    
@api_view(['GET'])
def detalhe_servico(request, id):
    try:
        servico = Servico.objects.get(id=id)
    except Servico.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ServicoSerializer(servico)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['GET'])
def listar_agendamento(request):
    if request.method == 'GET':
        agendamento = Agendamento.objects.all()
        serializer = AgendamentoSerializer(agendamento, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])    
def criar_agendamento(request):
    if request.method == 'POST':
        serializer = AgendamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET'])
def detalhe_agendamento(request, id):
    try:
        agendamento = Agendamento.objects.get(id=id)
    except Agendamento.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = AgendamentoSerializer(agendamento)
    return Response(serializer.data, status=status.HTTP_200_OK)