from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('<int:receita_id>', receita, name='receita'),
    path('buscar', buscar, name='buscar'),
    path('cria/receita', cria_receita, name='cria_receita'),
    path('editar/<int:receita_id>', editar_receita, name='editar_receita'),
    path('deletar/<int:receita_id>', deletar_receita, name='deletar_receita'),
    path('atualiza/<int:receita_id>', atualiza_receita, name='atualiza_receita'),

]
