from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from apps.receitas.models import Receita


def cadastro(request):
    """Cadastra uma nova pessoa no sistema"""
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if campo_vazio(nome):
            messages.error(request, 'O campo nome não pode ficar em branco.')
            return redirect('cadastro')
        if campo_vazio(email):
            messages.error(request, 'O campo senha não pode ficar em branco.')
            return redirect('cadastro')
        if campo_vazio(senha2):
            messages.error(request, 'O campo senha2 não pode ficar em branco.')
            return redirect('cadastro')
        if senhas_diferentes(senha, senha2):
            messages.error(request, 'Senhas não conferem. Precisam ser iguais.')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Usuário já existente.')
            return redirect('cadastro')
        if User.objects.filter(username=nome).exists():
            messages.error(request, 'Usuário já existente.')
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        messages.success(request, 'Usuário cadastrado com sucesso.')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')


def login(request):
    """Realiza o ‘login’ de uma pessoa no sistema"""
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if campo_vazio(email) or campo_vazio(senha):
            messages.error(request, 'Senha ou Login inválidos. Tente novamente.')
            return redirect('login')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Login realizado com sucesso.')
                return redirect('dashboard')
            else:
                messages.error(request, 'Email ou senha incorreta. Tente novamente.')
    return render(request, 'usuarios/login.html')


def logout(request):
    """Realiza a saída de uma pessoa do sistema. Redirecionado para a página principal da aplicação"""
    auth.logout(request)
    return redirect('index')


def dashboard(request):
    """Após o 'login' de uma pessoa no sistema, é redirecionada para dashboard para criar e editar receitas."""
    if request.user.is_authenticated:
        id_usuario = request.user.id
        receita = Receita.objects.order_by('-data_receita').filter(pessoa=id_usuario)

        dados = {
            'receitas': receita
        }

        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')


def campo_vazio(campo):
    """Verifica se os campos a serem editados estão vazios."""
    return not campo.strip()


def senhas_diferentes(senha, senha2):
    """Verifica se as senhas digitadas/fornecidas são diferentes."""
    return senha != senha2
