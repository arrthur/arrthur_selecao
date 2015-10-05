# -*- coding: utf-8 -*-
from django.db import models



class Categoria(models.Model):
    nome    = models.CharField('Nome da categoria', max_length=100, null = False)
    
    class Meta:
        app_label = 'categoria'
        
    def __unicode__(self):
        return 'id: %d, nome: %s' % (self.id, self.nome)
    
    
    