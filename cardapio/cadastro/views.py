# -*- coding:  utf-8 -*-
from django.db.models import Q

# Create your views here
from django.views.generic import ListView
from rest_framework import viewsets
from cadastro.forms import ItemCardapioForm
from cadastro.models import ItemCardapio
from cadastro.serializers import ItemCardapioSerializer


class ItemCardapioViewSet(viewsets.ModelViewSet):
    queryset = ItemCardapio.objects.prefetch_related('ingredienteitem_set').all()
    serializer_class = ItemCardapioSerializer

class Index(ListView):
    model = ItemCardapio
    template_name = 'index.html'
    form_class = ItemCardapioForm

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        busca = ''
        valor = ''
        result = ''
        try:
            busca = request.GET['busca']
            valor = request.GET['valor']
        except:
            pass
        try:
            if busca and valor == 'maior-preco':
                self.object_list = self.get_queryset().filter(Q(nome__icontains=busca) | Q(categoria__nome__icontains=busca)).order_by('categoria','-valor')
            elif busca or valor == 'menor-preco':
                self.object_list = self.get_queryset().filter(Q(nome__icontains=busca) | Q(categoria__nome__icontains=busca)).order_by('categoria','valor')

            if not busca:
                if valor == 'maior-preco':
                    self.object_list = self.get_queryset().order_by('categoria','-valor')
                elif valor == 'menor-preco':
                    self.object_list = self.get_queryset().order_by('categoria','valor')
        except:
            self.object_list = self.get_queryset()


        return self.render_to_response(self.get_context_data(object_list=self.object_list))