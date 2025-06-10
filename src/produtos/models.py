from django.db import models
from filial.models import Filial

class Produto(models.Model):
    indice = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quant = models.IntegerField()
    id_filial = models.ForeignKey(
        Filial,
        on_delete=models.CASCADE,
        db_column='id_filial'
    )
    descricao = models.TextField(blank=True, null=True)
    tipo = models.CharField(max_length=50)

    class Meta:
        db_table = 'produto'

    def __str__(self):
        return f"{self.nome} ({self.tipo})"
