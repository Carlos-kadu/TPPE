from django.db import models
from empresa.models import Empresa

class Filial(models.Model):
    id_filial = models.AutoField(primary_key=True)

    nome_cidade = models.CharField(max_length=100)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='filiais', db_column='id_empresa')

    class Meta:
        db_table = 'filial'

    def __str__(self):
        return self.nome_cidade

    @property
    def qtd_produtos(self):
        return self.produtos.count()

    def adc_item(self, produto):
        produto.filial = self
        produto.save()

    def editar_item(self, produto, quantidade):
        produto.quant = quantidade
        produto.save()

    def excluir_item(self, indice):
        produto = self.produtos.filter(indice=indice).first()
        if produto:
            produto.delete()

    def buscar_item(self, nome):
        return self.produtos.filter(nome__iexact=nome).first()

    def obter_caracteristicas_principais(self):
        return [
            [p.nome, str(p.preco), str(p.quant), self.nome_cidade, p.__class__.__name__]
            for p in self.produtos.all()
        ]

    def editar_filial(self, **kwargs):
        for attr, value in kwargs.items():
            if hasattr(self, attr):
                setattr(self, attr, value)
        self.save()

    def visualizar_filial(self):
        return {
            'id_filial': self.id_filial,
            'nome_cidade': self.nome_cidade,
            'empresa': self.empresa_id,
            'qtd_produtos': self.qtd_produtos
        }

    def deletar_filial(self):
        self.delete()
