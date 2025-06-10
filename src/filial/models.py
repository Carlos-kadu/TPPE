from django.db import models
from empresa.models import Empresa

class Filial(models.Model):
    id_filial = models.AutoField(primary_key=True)

    nome_cidade = models.CharField(max_length=100)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='filiais', db_column='id_empresa')
    qtd_produtos = models.IntegerField(default=0)

    class Meta:
        db_table = 'filial'

    def __str__(self):
        return self.nome_cidade
