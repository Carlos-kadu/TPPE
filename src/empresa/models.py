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

    def adc_filial(self, filial):
        if self.filiais.count() < self.num_max_filiais:
            filial.empresa = self
            filial.save()
            self.qtd_filiais = self.filiais.count()
            self.save()

    def excluir_filial(self, filial):
        filial.delete()
        self.qtd_filiais = self.filiais.count()
        self.save()

    def buscar_filial(self, nome):
        return self.filiais.filter(nome_cidade__iexact=nome).first()
