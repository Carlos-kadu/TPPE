from rest_framework import serializers
from .models import Alimentacao, Vestuario, UtilidadesDomesticas

class ProdutoBaseSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=100)
    preco = serializers.DecimalField(max_digits=10, decimal_places=2)
    quant = serializers.IntegerField()
    filial = serializers.PrimaryKeyRelatedField(read_only=True)
    descricao = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    indice = serializers.IntegerField(read_only=True)

class AlimentacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alimentacao
        fields = '__all__'

class VestuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vestuario
        fields = '__all__'

class UtilidadesDomesticasSerializer(serializers.ModelSerializer):
    class Meta:
        model = UtilidadesDomesticas
        fields = '__all__'