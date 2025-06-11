import pytest
from rest_framework.test import APIClient
from empresa.models import Empresa
from filial.models import Filial

@pytest.mark.django_db
def test_criar_produto():
    client = APIClient()

    empresa = Empresa.objects.create(
        razao_social="Empresa Teste",
        cnpj="00.000.000/0001-00",
        num_max_filiais=10
    )
    filial = Filial.objects.create(
        nome_cidade="Cidade Teste",
        empresa=empresa
    )

    data = {
        "nome": "Arroz",
        "preco": "5.99",
        "quant": 20,
        "id_filial": filial.id_filial,
        "descricao": "Arroz branco tipo 1",
        "tipo": "Alimentacao"
    }

    response = client.post("/api/produtos/", data, format='json')
    assert response.status_code == 201
    assert response.data['nome'] == "Arroz"
