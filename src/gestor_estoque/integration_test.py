import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from empresa.models import Empresa
from filial.models import Filial
from produtos.models import Alimentacao, Vestuario, UtilidadesDomesticas

@pytest.mark.django_db
def test_fluxo_integração_completo():
    client = APIClient()

    empresa_data = {"razao_social": "Empresa Integrada", "cnpj": "12.345.678/0001-99", "qtd_filiais": 0, "num_max_filiais": 5}
    empresa_resp = client.post(reverse('empresa-list'), empresa_data)
    assert empresa_resp.status_code == 201
    empresa_id = empresa_resp.data['id_empresa']

    filial_data = {"nome_cidade": "Filial Central", "empresa": empresa_id, "qtd_produtos": 0}
    filial_resp = client.post(reverse('filial-list'), filial_data)
    assert filial_resp.status_code == 201
    filial_id = filial_resp.data['id_filial']

    alimentacao_data = {"nome": "Arroz Integral", "preco": 10.0, "quant": 10, "descricao": "Integral", "peso": 1.0, "vegetariano": True, "filial": filial_id}
    vestuario_data = {"nome": "Camiseta Polo", "preco": 50.0, "quant": 5, "descricao": "Algodão", "tamanho": 42, "genero": "M", "filial": filial_id}
    utilidade_data = {"nome": "Panela", "preco": 80.0, "quant": 2, "descricao": "Antiaderente", "material": "Alumínio", "marca": "Tramontina", "caracteristicas": "Com tampa", "filial": filial_id}
    resp_a = client.post(reverse('alimentacao-list'), alimentacao_data)
    resp_v = client.post(reverse('vestuario-list'), vestuario_data)
    resp_u = client.post(reverse('utilidadesdomesticas-list'), utilidade_data)
    assert resp_a.status_code == 201
    assert resp_v.status_code == 201
    assert resp_u.status_code == 201

    produtos_filial = Alimentacao.objects.filter(filial_id=filial_id)
    assert produtos_filial.count() == 1
    produtos_filial_v = Vestuario.objects.filter(filial_id=filial_id)
    assert produtos_filial_v.count() == 1
    produtos_filial_u = UtilidadesDomesticas.objects.filter(filial_id=filial_id)
    assert produtos_filial_u.count() == 1

    del_resp = client.delete(reverse('empresa-detail', args=[empresa_id]))
    assert del_resp.status_code == 204
    assert not Filial.objects.filter(id_filial=filial_id).exists()
    assert not Alimentacao.objects.filter(filial_id=filial_id).exists()
    assert not Vestuario.objects.filter(filial_id=filial_id).exists()
    assert not UtilidadesDomesticas.objects.filter(filial_id=filial_id).exists() 