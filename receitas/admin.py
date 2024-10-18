from django.contrib import admin
from .models import Receita


class ListandoReceitas(admin.ModelAdmin):
    list_display = ("id", "nome_receita", "categoria", "pessoa", "publicada")
    list_display_links = ("id", "nome_receita")
    search_fields = ("nome_receita",)
    # Nesse campo, precisa passar um param tipo tupla, por isso a vírgula após o param passado.
    list_filter = ("categoria", )
    list_editable = ("publicada", )
    list_per_page = 10


admin.site.register(Receita, ListandoReceitas)
