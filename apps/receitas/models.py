from django.db import models
from django.contrib.auth.models import User


class Receita(models.Model):
    pessoa = models.ForeignKey(User, on_delete=models.SET_DEFAULT, null=True, default=None, blank=True)
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receita = models.DateTimeField(auto_now_add=True, blank=True)
    foto_receita = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)
    publicada = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_receita
