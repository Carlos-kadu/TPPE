from django.db import models


class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    razao_social = models.CharField(max_length=100, unique=True)
    cnpj = models.CharField(max_length=18, unique=True)
    num_max_filiais = models.IntegerField()

    class Meta:
        db_table = 'empresa'

    def __str__(self):
        return self.razao_social

    @property
    def qtd_filiais(self):
        return self.filiais.count()

    def adc_filial(self, filial):
        if self.filiais.count() < self.num_max_filiais:
            filial.empresa = self
            filial.save()

    def excluir_filial(self, filial):
        filial.delete()

    def buscar_filial(self, nome):
        return self.filiais.filter(nome_cidade__iexact=nome).first()

    def editar_empresa(self, **kwargs):
        for attr, value in kwargs.items():
            if hasattr(self, attr):
                setattr(self, attr, value)
        self.save()

    def visualizar_empresa(self):
        return {
            'id_empresa': self.id_empresa,
            'razao_social': self.razao_social,
            'cnpj': self.cnpj,
            'num_max_filiais': self.num_max_filiais,
            'qtd_filiais': self.qtd_filiais
        }

    def deletar_empresa(self):
        self.delete()
