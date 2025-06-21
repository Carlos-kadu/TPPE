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

    def adc_item(self, produto):
        produto.filial = self
        produto.save()
        self.qtd_produtos = self.produtos.count()
        self.save()

    def editar_item(self, produto, quantidade):
        produto.quant = quantidade
        produto.save()

    def excluir_item(self, indice):
        produto = self.produtos.filter(indice=indice).first()
        if produto:
            produto.delete()
            self.qtd_produtos = self.produtos.count()
            self.save()

    def buscar_item(self, nome):
        return self.produtos.filter(nome__iexact=nome).first()

    def obter_caracteristicas_principais(self):
        return [
            [p.nome, str(p.preco), str(p.quant), self.nome_cidade, p.__class__.__name__]
            for p in self.produtos.all()
        ]
