import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from filial.models import Filial
from empresa.models import Empresa


@pytest.mark.django_db
def test_create_filial():
    empresa = Empresa.objects.create(
        razao_social="Empresa F",
        cnpj="55.555.555/0001-55",
        qtd_filiais=0,
        num_max_filiais=5
    )
    client = APIClient()
    data = {
        "nome_cidade": "Cidade Teste",
        "empresa": empresa.id_empresa
    }
    response = client.post(reverse('filial-list'), data)
    assert response.status_code == 201
    assert Filial.objects.filter(nome_cidade="Cidade Teste").exists()


@pytest.mark.django_db
def test_get_filiais():
    empresa = Empresa.objects.create(
        razao_social="Empresa F2",
        cnpj="66.666.666/0001-66",
        qtd_filiais=0,
        num_max_filiais=5
    )
    Filial.objects.create(nome_cidade="Cidade 1", empresa=empresa)
    client = APIClient()
    response = client.get(reverse('filial-list'))
    assert response.status_code == 200
    assert len(response.data) >= 1


@pytest.mark.django_db
def test_update_filial():
    empresa = Empresa.objects.create(
        razao_social="Empresa F3",
        cnpj="77.777.777/0001-77",
        qtd_filiais=0,
        num_max_filiais=5
    )
    filial = Filial.objects.create(nome_cidade="Cidade X", empresa=empresa)
    client = APIClient()
    url = reverse('filial-detail', args=[filial.id_filial])
    data = {
        "nome_cidade": "Cidade Param",
        "empresa": empresa.id_empresa
    }
    response = client.put(url, data)
    assert response.status_code == 200
    filial.refresh_from_db()
    assert filial.nome_cidade == "Cidade Param"


@pytest.mark.django_db
def test_delete_filial():
    empresa = Empresa.objects.create(
        razao_social="Empresa F4",
        cnpj="88.888.888/0001-88",
        qtd_filiais=0,
        num_max_filiais=5
    )
    filial = Filial.objects.create(nome_cidade="Cidade Del", empresa=empresa)
    client = APIClient()
    url = reverse('filial-detail', args=[filial.id_filial])
    response = client.delete(url)
    assert response.status_code == 204
    assert not Filial.objects.filter(id_filial=filial.id_filial).exists()
