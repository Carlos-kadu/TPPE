from django.db import models
from filial.models import Filial

class Produto(models.Model):
    indice = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quant = models.IntegerField()
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'produto'
        abstract = True

    def __str__(self):
        return f"{self.nome} ({self.__class__.__name__})"

    def editar_caracteristica(self, nome, preco, quant, filial, descricao):
        self.nome = nome
        self.preco = preco
        self.quant = quant
        self.filial = filial
        self.descricao = descricao
        self.save()

    def editar_produto(self, **kwargs):
        for attr, value in kwargs.items():
            if hasattr(self, attr):
                setattr(self, attr, value)
        self.save()

    def visualizar_produto(self):
        return {
            'indice': self.indice,
            'nome': self.nome,
            'preco': float(self.preco),
            'quant': self.quant,
            'descricao': self.descricao
        }

    def deletar_produto(self):
        self.delete()

class Alimentacao(Produto):
    filial = models.ForeignKey(
        Filial,
        on_delete=models.CASCADE,
        related_name='alimentacoes',
        db_column='id_filial'
    )
    peso = models.FloatField()
    vegetariano = models.BooleanField()

    class Meta:
        db_table = 'alimentacao'

class Vestuario(Produto):
    filial = models.ForeignKey(
        Filial,
        on_delete=models.CASCADE,
        related_name='vestuarios',
        db_column='id_filial'
    )
    tamanho = models.IntegerField()
    genero = models.CharField(max_length=20)

    class Meta:
        db_table = 'vestuario'

class UtilidadesDomesticas(Produto):
    filial = models.ForeignKey(
        Filial,
        on_delete=models.CASCADE,
        related_name='utilidades_domesticas',
        db_column='id_filial'
    )
    material = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    caracteristicas = models.TextField()

    class Meta:
        db_table = 'utilidades_domesticas'
