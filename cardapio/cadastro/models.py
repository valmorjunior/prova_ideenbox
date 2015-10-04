from django.db import models

# Create your models here.

class Categoria(models.Model):

    class Meta:
        app_label = 'cadastro'
        verbose_name = 'Categoria'
        verbose_name_plural = verbose_name+'s'
        ordering = ['id']

    nome = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nome

class Ingrediente(models.Model):

    class Meta:
        app_label = 'cadastro'
        verbose_name = 'Ingrediente'
        verbose_name_plural = verbose_name+'s'

    nome = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nome

class ItemCardapio(models.Model):

    class Meta:
        app_label = 'cadastro'
        verbose_name = 'Item do Cardapio'
        verbose_name = 'Itens do Cardapio'
        ordering = ['categoria__id']

    categoria = models.ForeignKey('Categoria')
    nome = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
        return '%s - %s' % (self.nome, self.valor)

class IngredienteItem(models.Model):

    class Meta:
        app_label = 'cadastro'

    item_cardapio = models.ForeignKey('ItemCardapio')
    ingrediente = models.ForeignKey('Ingrediente')