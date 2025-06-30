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
    def validate(self, data):
        if data.get('peso', 0) < 0:
            raise serializers.ValidationError({'peso': 'O peso não pode ser negativo.'})
        if data.get('quant', 0) < 0:
            raise serializers.ValidationError({'quant': 'A quantidade não pode ser negativa.'})
        if data.get('preco', 0) < 0:
            raise serializers.ValidationError({'preco': 'O preço não pode ser negativo.'})
        return data
    class Meta:
        model = Alimentacao
        fields = '__all__'

class VestuarioSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if data.get('tamanho', 0) < 0:
            raise serializers.ValidationError({'tamanho': 'O tamanho não pode ser negativo.'})
        if data.get('quant', 0) < 0:
            raise serializers.ValidationError({'quant': 'A quantidade não pode ser negativa.'})
        if data.get('preco', 0) < 0:
            raise serializers.ValidationError({'preco': 'O preço não pode ser negativo.'})
        return data
    class Meta:
        model = Vestuario
        fields = '__all__'

class UtilidadesDomesticasSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if data.get('quant', 0) < 0:
            raise serializers.ValidationError({'quant': 'A quantidade não pode ser negativa.'})
        if data.get('preco', 0) < 0:
            raise serializers.ValidationError({'preco': 'O preço não pode ser negativo.'})
        return data
    class Meta:
        model = UtilidadesDomesticas
        fields = '__all__'