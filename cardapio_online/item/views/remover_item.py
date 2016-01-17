'''
Created on 17/01/2016

@author: Arthur
'''
from django.shortcuts import redirect
from item.models.item import Item

def remover_item(request, id_item):
    item = Item.objects.get(pk=id_item)
    item.delete()

    
    return redirect('listar_item_acesso')