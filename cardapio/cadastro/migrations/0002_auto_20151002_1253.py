# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Ingrediente',
                'verbose_name_plural': 'Ingredientes',
            },
        ),
        migrations.CreateModel(
            name='IngredienteItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ingrediente', models.ForeignKey(to='cadastro.Ingrediente')),
            ],
        ),
        migrations.RemoveField(
            model_name='itemcardapio',
            name='ingredientes',
        ),
        migrations.AddField(
            model_name='ingredienteitem',
            name='item_cardapio',
            field=models.ForeignKey(to='cadastro.ItemCardapio'),
        ),
    ]
