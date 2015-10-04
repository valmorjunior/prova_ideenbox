from rest_framework import serializers
from cadastro.models import Categoria, Ingrediente, ItemCardapio, IngredienteItem


class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        field = ('id','nome')

class IngredienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingrediente
        field = ('id','nome')

class IngredienteItemSerializer(serializers.ModelSerializer):

    ingrediente = IngredienteSerializer()

    class Meta:
        model = IngredienteItem
        field = ('ingrediente')

class ItemCardapioSerializer(serializers.ModelSerializer):

    categoria = CategoriaSerializer()

    class Meta:
        model = ItemCardapio
        field = ('id','nome','categoria')