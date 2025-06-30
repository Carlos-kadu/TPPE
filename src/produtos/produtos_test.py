import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from filial.models import Filial
from empresa.models import Empresa
from produtos.models import Alimentacao, Vestuario, UtilidadesDomesticas


@pytest.fixture
def filial():
    empresa = Empresa.objects.create(
        razao_social="Empresa P",
        cnpj="99.999.999/0001-99",
        num_max_filiais=5
    )
    return Filial.objects.create(nome_cidade="Cidade P", empresa=empresa)


@pytest.mark.django_db
@pytest.mark.parametrize(
    "endpoint,model,data",
    [
        (
            "alimentacao-list",
            Alimentacao,
            {
                "nome": "Arroz",
                "preco": 10.5,
                "quant": 5,
                "descricao": "Integral",
                "peso": 1.0,
                "vegetariano": True,
            },
        ),
        (
            "vestuario-list",
            Vestuario,
            {
                "nome": "Camiseta",
                "preco": 30.0,
                "quant": 10,
                "descricao": "Algodão",
                "tamanho": 42,
                "genero": "M",
            },
        ),
        (
            "utilidadesdomesticas-list",
            UtilidadesDomesticas,
            {
                "nome": "Panela",
                "preco": 50.0,
                "quant": 2,
                "descricao": "Antiaderente",
                "material": "Alumínio",
                "marca": "Tramontina",
                "caracteristicas": "Com tampa",
            },
        ),
    ],
)
def test_create_produto(endpoint, model, data, filial):
    client = APIClient()
    data = dict(data)
    data["filial"] = filial.id_filial
    response = client.post(reverse(endpoint), data)
    assert response.status_code == 201
    assert model.objects.filter(
        nome=data["nome"]
    ).exists()


@pytest.mark.django_db
@pytest.mark.parametrize(
    "endpoint,model",
    [
        ("alimentacao-list", Alimentacao),
        ("vestuario-list", Vestuario),
        ("utilidadesdomesticas-list", UtilidadesDomesticas),
    ],
)
def test_get_produtos(endpoint, model, filial):
    if model == Alimentacao:
        model.objects.create(
            nome="Feijao",
            preco=8.0,
            quant=3,
            descricao="Carioca",
            peso=1.0,
            vegetariano=True,
            filial=filial,
        )
    elif model == Vestuario:
        model.objects.create(
            nome="Calca",
            preco=80.0,
            quant=2,
            descricao="Jeans",
            tamanho=40,
            genero="F",
            filial=filial,
        )
    else:
        model.objects.create(
            nome="Prato",
            preco=15.0,
            quant=6,
            descricao="Cerâmica",
            material="Cerâmica",
            marca="Oxford",
            caracteristicas="Raso",
            filial=filial,
        )
    client = APIClient()
    response = client.get(reverse(endpoint))
    assert response.status_code == 200
    assert len(response.data) >= 1


@pytest.mark.django_db
@pytest.mark.parametrize(
    "endpoint,model,field,value",
    [
        ("alimentacao-detail", Alimentacao, "preco", 12.0),
        ("vestuario-detail", Vestuario, "tamanho", 44),
        (
            "utilidadesdomesticas-detail",
            UtilidadesDomesticas,
            "marca",
            "Brinox"
        ),
    ],
)
def test_update_produto(endpoint, model, field, value, filial):
    if model == Alimentacao:
        obj = model.objects.create(
            nome="Macarrao",
            preco=5.0,
            quant=2,
            descricao="Espaguete",
            peso=0.5,
            vegetariano=False,
            filial=filial,
        )
        data = {
            "nome": obj.nome,
            "preco": obj.preco,
            "quant": obj.quant,
            "descricao": obj.descricao,
            "peso": obj.peso,
            "vegetariano": obj.vegetariano,
            "filial": filial.id_filial,
        }
    elif model == Vestuario:
        obj = model.objects.create(
            nome="Bermuda",
            preco=40.0,
            quant=1,
            descricao="Jeans",
            tamanho=38,
            genero="M",
            filial=filial,
        )
        data = {
            "nome": obj.nome,
            "preco": obj.preco,
            "quant": obj.quant,
            "descricao": obj.descricao,
            "tamanho": obj.tamanho,
            "genero": obj.genero,
            "filial": filial.id_filial,
        }
    else:
        obj = model.objects.create(
            nome="Talher",
            preco=20.0,
            quant=4,
            descricao="Inox",
            material="Inox",
            marca="Tramontina",
            caracteristicas="Faca",
            filial=filial,
        )
        data = {
            "nome": obj.nome,
            "preco": obj.preco,
            "quant": obj.quant,
            "descricao": obj.descricao,
            "material": obj.material,
            "marca": obj.marca,
            "caracteristicas": obj.caracteristicas,
            "filial": filial.id_filial,
        }
    data[field] = value
    client = APIClient()
    url = reverse(endpoint, args=[obj.indice])
    response = client.put(url, data)
    assert response.status_code == 200
    obj.refresh_from_db()
    assert getattr(obj, field) == value


@pytest.mark.django_db
@pytest.mark.parametrize(
    "endpoint,model",
    [
        ("alimentacao-detail", Alimentacao),
        ("vestuario-detail", Vestuario),
        ("utilidadesdomesticas-detail", UtilidadesDomesticas),
    ],
)
def test_delete_produto(endpoint, model, filial):
    if model == Alimentacao:
        obj = model.objects.create(
            nome="Farinha",
            preco=3.0,
            quant=1,
            descricao="Trigo",
            peso=1.0,
            vegetariano=True,
            filial=filial,
        )
    elif model == Vestuario:
        obj = model.objects.create(
            nome="Saia",
            preco=60.0,
            quant=1,
            descricao="Jeans",
            tamanho=36,
            genero="F",
            filial=filial,
        )
    else:
        obj = model.objects.create(
            nome="Copo",
            preco=5.0,
            quant=12,
            descricao="Vidro",
            material="Vidro",
            marca="Nadir",
            caracteristicas="Transparente",
            filial=filial,
        )
    client = APIClient()
    url = reverse(endpoint, args=[obj.indice])
    response = client.delete(url)
    assert response.status_code == 204
    assert not model.objects.filter(indice=obj.indice).exists()


@pytest.mark.django_db
@pytest.mark.parametrize(
    "endpoint,data,erro_campo",
    [
        (
            "alimentacao-list", {
                "nome": "Arroz",
                "preco": 10.5,
                "quant": -1,
                "descricao": "Integral",
                "peso": 1.0,
                "vegetariano": True,
            },
            'quant'
        ),
        (
            "alimentacao-list",
            {
                "nome": "Arroz",
                "preco": 10.5,
                "quant": 1,
                "descricao": "Integral",
                "peso": -2.0,
                "vegetariano": True,
            },
            'peso'
        ),
        (
            "alimentacao-list",
            {
                "nome": "Arroz",
                "preco": -5.0,
                "quant": 1,
                "descricao": "Integral",
                "peso": 1.0,
                "vegetariano": True,
            },
            'preco'
        ),
        (
            "vestuario-list",
            {
                "nome": "Camiseta",
                "preco": 30.0,
                "quant": -3,
                "descricao": "Algodão",
                "tamanho": 42,
                "genero": "M",
            },
            'quant'
        ),
        (
            "vestuario-list",
            {
                "nome": "Camiseta",
                "preco": 30.0,
                "quant": 3,
                "descricao": "Algodão",
                "tamanho": -42,
                "genero": "M",
            },
            'tamanho'
        ),
        (
            "vestuario-list",
            {
                "nome": "Camiseta",
                "preco": -30.0,
                "quant": 3,
                "descricao": "Algodão",
                "tamanho": 42,
                "genero": "M",
            },
            'preco'
        ),
        (
            "utilidadesdomesticas-list",
            {
                "nome": "Panela",
                "preco": 50.0,
                "quant": -2,
                "descricao": "Antiaderente",
                "material": "Alumínio",
                "marca": "Tramontina",
                "caracteristicas": "Com tampa",
            },
            'quant'
        ),
        (
            "utilidadesdomesticas-list",
            {
                "nome": "Panela",
                "preco": -50.0,
                "quant": 2,
                "descricao": "Antiaderente",
                "material": "Alumínio",
                "marca": "Tramontina",
                "caracteristicas": "Com tampa",
            },
            'preco'
        ),
    ],
)
def test_create_produto_valores_invalidos(endpoint, data, erro_campo, filial):
    client = APIClient()
    data = dict(data)
    data["filial"] = filial.id_filial
    response = client.post(reverse(endpoint), data)
    assert response.status_code == 400
    assert erro_campo in response.data
