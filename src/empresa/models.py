from django.db import models

class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    razao_social = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True)
    qtd_filiais = models.IntegerField(default=0)
    num_max_filiais = models.IntegerField()

    class Meta:
        db_table = 'empresa'

    def __str__(self):
        return self.razao_social
