# -*- coding: utf-8 -*-

from django.contrib import messages
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from item.forms.item_form import ItemForm
from item.models.item import Item




def editar_item(request, id_item=None):
    if id_item:
        instance = Item.objects.get(pk=id_item)
        
    else:
        instance = None
        
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=instance)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Adicionado com sucesso")
            return redirect('listar_item_acesso')
    
    else:
        
        form = ItemForm(instance=instance)
        
        
    
    return render_to_response('editar_item.html', locals(),context_instance=RequestContext(request))
        
        
        
    
        
        
    