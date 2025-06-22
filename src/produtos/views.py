from django.shortcuts import render
from rest_framework import viewsets
from .models import Alimentacao, Vestuario, UtilidadesDomesticas
from .serializers import AlimentacaoSerializer, VestuarioSerializer, UtilidadesDomesticasSerializer

class AlimentacaoViewSet(viewsets.ModelViewSet):
    queryset = Alimentacao.objects.all()
    serializer_class = AlimentacaoSerializer

class VestuarioViewSet(viewsets.ModelViewSet):
    queryset = Vestuario.objects.all()
    serializer_class = VestuarioSerializer

class UtilidadesDomesticasViewSet(viewsets.ModelViewSet):
    queryset = UtilidadesDomesticas.objects.all()
    serializer_class = UtilidadesDomesticasSerializer
