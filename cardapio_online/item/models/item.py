# -*- coding: utf-8 -*-
from django.db import models
from ingrediente.models.ingrediente import Ingrediente
from categoria.models.categoria import Categoria

CATEGORIA_CHOICE = (('', '----------'),
                ('ENTRADAS',('ENTRADAS')),
                ('PRINCIPAL',('PRINCIPAL')),
                ('SOBREMESA',('SOBREMESA')),
                ('BEBIDAS',('BEBIDAS')),               
                )

class Item(models.Model):
    nome    = models.CharField('Nome do item', max_length=100, null = False)
    valor = models.DecimalField('Valor', decimal_places=2, max_digits=9)
    tempo_preparo = models.TimeField("Tempo de preparo")
    ingrediente = models.ManyToManyField(Ingrediente)
    #categoria   = models.CharField('Categoria', max_length=100, choices=CATEGORIA_CHOICE)
    categoria = models.ForeignKey(Categoria)
    
    def __unicode__(self):
        return self.nome
    
    class Meta:
        app_label = 'item'
        
    def ingredientes(self):
        return self.ingrediente.all()