from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters
from .models import Alimentacao, Vestuario, UtilidadesDomesticas
from .serializers import AlimentacaoSerializer, VestuarioSerializer, UtilidadesDomesticasSerializer
from django.db.models import Q

class AlimentacaoViewSet(viewsets.ModelViewSet):
    queryset = Alimentacao.objects.all()
    serializer_class = AlimentacaoSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        filial_id = self.request.query_params.get('filial')
        baixo_estoque = self.request.query_params.get('baixo_estoque')
        if filial_id:
            queryset = queryset.filter(filial_id=filial_id)
        if baixo_estoque:
            try:
                threshold = int(self.request.query_params.get('limite', 20))
            except Exception:
                threshold = 20
            queryset = queryset.filter(quant__lte=threshold)
        return queryset

class VestuarioViewSet(viewsets.ModelViewSet):
    queryset = Vestuario.objects.all()
    serializer_class = VestuarioSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        filial_id = self.request.query_params.get('filial')
        baixo_estoque = self.request.query_params.get('baixo_estoque')
        if filial_id:
            queryset = queryset.filter(filial_id=filial_id)
        if baixo_estoque:
            try:
                threshold = int(self.request.query_params.get('limite', 20))
            except Exception:
                threshold = 20
            queryset = queryset.filter(quant__lte=threshold)
        return queryset

class UtilidadesDomesticasViewSet(viewsets.ModelViewSet):
    queryset = UtilidadesDomesticas.objects.all()
    serializer_class = UtilidadesDomesticasSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        filial_id = self.request.query_params.get('filial')
        baixo_estoque = self.request.query_params.get('baixo_estoque')
        if filial_id:
            queryset = queryset.filter(filial_id=filial_id)
        if baixo_estoque:
            try:
                threshold = int(self.request.query_params.get('limite', 20))
            except Exception:
                threshold = 20
            queryset = queryset.filter(quant__lte=threshold)
        return queryset
