from django.db import models
from pessoas.models import Pessoa


class Receita(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.SET_DEFAULT, null=True, default=None)
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receita = models.DateTimeField(auto_now_add=True, blank=True)
