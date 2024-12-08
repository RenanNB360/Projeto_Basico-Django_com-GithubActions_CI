import pytest
from django.urls import reverse

from core.models import Produto


@pytest.mark.django_db
def test_index(client):
    Produto.objects.create(nome='Produto 1', preco=10.0, estoque=100)

    resposta = client.get('')

    assert resposta.status_code == 200

    assert 'titulo' in resposta.context
    assert resposta.context['titulo'] == 'Programação Web com Django Framework'

    assert 'etapa' in resposta.context
    assert resposta.context['etapa'] == 'Conceitos'

    assert 'produtos' in resposta.context
    assert len(resposta.context['produtos']) == 1

    produtos_esperados = [
        {'nome': 'Produto 1', 'preco': 10.0, 'estoque': 100},
    ]

    produtos_retorno = list(resposta.context['produtos'].values('nome', 'preco', 'estoque'))
    assert produtos_retorno == produtos_esperados


@pytest.mark.django_db
def test_contato(client):
    resposta = client.get(reverse('contato'))

    assert resposta.status_code == 200


@pytest.mark.django_db
def test_produto(client):
    produto = Produto.objects.create(nome='Produto 1', preco=105.6, estoque=50)

    url = reverse('produto', kwargs={'pk': produto.id})
    resposta = client.get(url)

    assert resposta.status_code == 200

    assert 'produto' in resposta.context
    assert resposta.context['produto'] == produto


@pytest.mark.django_db
def test_produto_not_found(client):
    url = reverse('produto', kwargs={'pk': 999})
    resposta = client.get(url)

    assert resposta.status_code == 404


def test_error404(client):
    resposta = client.get('/url_inexistente/')

    assert resposta.status_code == 404
    assert '404' in resposta.content.decode()
