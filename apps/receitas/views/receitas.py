from django.shortcuts import render, get_object_or_404, redirect
from apps.receitas.models import Receita
from django.contrib.auth.models import User
from django.core.paginator import Paginator


def index(request):
    """Mostra a página inicial da aplicação com as receitas com status publicada.
    Configura a quantidade de receitas por páginas e um modo de navegar em outras receitas publicadas."""
    receitas = Receita.objects.order_by("-data_receita").filter(publicada=True)
    paginador = Paginator(receitas, 6)
    page = request.GET.get('page')
    receitas_por_pagina = paginador.get_page(page)

    dados = {
        'receitas': receitas_por_pagina
    }

    return render(request, "receitas/index.html", dados)


def receita(request, receita_id):
    """Mostra a receita na página inicial."""
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_exibida = {
        'receita': receita
    }

    return render(request, "receitas/receita.html", receita_exibida)


def cria_receita(request):
    """Método para criação de receita a partir da model Receita."""
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita']
        user = get_object_or_404(User, pk=request.user.id)
        receita = Receita.objects.create(pessoa=user, nome_receita=nome_receita, ingredientes=ingredientes, modo_preparo=modo_preparo,
                                         tempo_preparo=tempo_preparo, rendimento=rendimento, categoria=categoria, foto_receita=foto_receita)
        receita.save()
        return redirect('dashboard')
    else:
        return render(request, 'receitas/cria_receita.html')


def editar_receita(request, receita_id):
    """Método para editar a receita que foi criada por uma pessoa."""
    receita = get_object_or_404(Receita, pk=receita_id)
    receita_a_editar = {'receita': receita}
    return render(request, 'receitas/edita_receita.html', receita_a_editar)


def deletar_receita(request, receita_id):
    """Método para deletar uma receita."""
    receita = get_object_or_404(Receita, pk=receita_id)
    receita.delete()
    return redirect('dashboard')


def atualiza_receita(request, receita_id):
    """Método para realizar alteração na receita criada por uma pessoa."""
    if request.method == 'POST':
        receita_id = request.POST['receita_id']
        r = Receita.objects.get(pk=receita_id)
        r.nome_receita = request.POST['nome_receita']
        r.ingredientes = request.POST['ingredientes']
        r.modo_preparo = request.POST['modo_preparo']
        r.tempo_preparo = request.POST['tempo_preparo']
        r.rendimento = request.POST['rendimento']
        r.categoria = request.POST['categoria']
        if 'foto_receita' in request.FILES:
            r.foto_receita = request.FILES['foto_receita']
        r.save()
        return redirect('dashboard')
