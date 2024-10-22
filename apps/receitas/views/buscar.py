from django.shortcuts import render
from apps.receitas.models import Receita


def buscar(request):
    """Método que ajuda na busca de uma receita a partir de um nome ou parte dele."""
    lista_receitas = Receita.objects.order_by("-data_receita").filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)

    dados = {
        'receitas': lista_receitas
    }

    return render(request, "receitas/buscar.html", dados)
