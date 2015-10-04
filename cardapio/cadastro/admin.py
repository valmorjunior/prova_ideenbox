from django.contrib import admin

# Register your models here.
from cadastro.models import Categoria, ItemCardapio, Ingrediente, IngredienteItem

admin.site.register(Categoria)
admin.site.register(Ingrediente)

class ItemIngredienteInline(admin.TabularInline):
    model = IngredienteItem
    extra = 1

class ItemCardapioAdmin(admin.ModelAdmin):
    inlines = [ItemIngredienteInline]

admin.site.register(ItemCardapio, ItemCardapioAdmin)
