from django.contrib import admin
from .models import Receita


class ListandoReceitas(admin.ModelAdmin):
    list_display = ("id", "nome_receita", "categoria")
    list_display_links = ("id", "nome_receita")
    search_fields = ("nome_receita",)
    # Nesse campo, precisa passar um param tipo tupla, por isso a vírgula após o param passado.
    list_filter = ("categoria", )
    list_per_page = 2


admin.site.register(Receita, ListandoReceitas)
