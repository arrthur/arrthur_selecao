# -*- coding: utf-8 -*-

from django.contrib import messages
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from ingrediente.models.ingrediente import Ingrediente
from ingrediente.forms.ingrediente_form import IngredienteForm



def editar_ingrediente(request, id_ingrediente=None):
    if id_ingrediente:
        instance = Ingrediente.objects.get(pk=id_ingrediente)
        
    else:
        instance = None
        
    if request.method == 'POST':
        form = IngredienteForm(request.POST, instance=instance)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Adicionado com sucesso")
            return redirect('listar_ingrediente')
    
    else:
        
        form = IngredienteForm(instance=instance)
        
        
    
    return render_to_response('editar_ingrediente.html', locals(),context_instance=RequestContext(request))
        
        
        
    
        
        
    