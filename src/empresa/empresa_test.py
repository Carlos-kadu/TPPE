import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from empresa.models import Empresa

@pytest.mark.django_db
def test_create_empresa():
    client = APIClient()
    data = {"razao_social": "Empresa Teste", "cnpj": "12.345.678/0001-99", "qtd_filiais": 0, "num_max_filiais": 10}
    response = client.post(reverse('empresa-list'), data)
    assert response.status_code == 201
    assert Empresa.objects.filter(razao_social="Empresa Teste").exists()

@pytest.mark.django_db
def test_get_empresas():
    Empresa.objects.create(razao_social="Empresa 1", cnpj="11.111.111/0001-11", qtd_filiais=0, num_max_filiais=5)
    client = APIClient()
    response = client.get(reverse('empresa-list'))
    assert response.status_code == 200
    assert len(response.data) >= 1

@pytest.mark.django_db
@pytest.mark.parametrize("field,value", [
    ("razao_social", "Empresa Param"),
    ("cnpj", "22.222.222/0001-22"),
    ("num_max_filiais", 15),
])
def test_update_empresa(field, value):
    empresa = Empresa.objects.create(razao_social="Empresa X", cnpj="33.333.333/0001-33", qtd_filiais=0, num_max_filiais=5)
    client = APIClient()
    url = reverse('empresa-detail', args=[empresa.id_empresa])
    data = {"razao_social": empresa.razao_social, "cnpj": empresa.cnpj, "qtd_filiais": empresa.qtd_filiais, "num_max_filiais": empresa.num_max_filiais}
    data[field] = value
    response = client.put(url, data)
    assert response.status_code == 200
    empresa.refresh_from_db()
    assert getattr(empresa, field) == value

@pytest.mark.django_db
def test_delete_empresa():
    empresa = Empresa.objects.create(razao_social="Empresa Del", cnpj="44.444.444/0001-44", qtd_filiais=0, num_max_filiais=5)
    client = APIClient()
    url = reverse('empresa-detail', args=[empresa.id_empresa])
    response = client.delete(url)
    assert response.status_code == 204
    assert not Empresa.objects.filter(id_empresa=empresa.id_empresa).exists()
