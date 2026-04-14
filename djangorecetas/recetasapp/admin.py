from django.contrib import admin
from .models import Ingrediente, Plato, LinaIngrediente, EntradaMenu

@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

class LinaIngredienteInline(admin.TabularInline):
    model = LinaIngrediente
    extra = 1

@admin.register(Plato)
class PlatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tempada')
    search_fields = ('nome',)
    list_filter = ('tempada',)
    inlines = [LinaIngredienteInline]

@admin.register(EntradaMenu)
class EntradaMenuAdmin(admin.ModelAdmin):
    list_display = ('data', 'momento', 'plato')
    list_filter = ('data', 'momento')
    date_hierarchy = 'data'
