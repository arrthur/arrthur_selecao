# -*- coding: utf-8 -*-
from django.db import models



class Ingrediente(models.Model):
    nome    = models.CharField('Nome do ingrediente', max_length=100, null = False)
    
    def __unicode__(self):
        return 'id: %d, nome: %s' % (self.id, self.nome)
    
    class Meta:
        app_label = 'ingrediente'
        
    