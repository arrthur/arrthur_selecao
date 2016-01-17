# -*- coding: utf-8 -*-

from django.contrib import messages
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from categoria.models.categoria import Categoria
from categoria.forms.categoria_form import CategoriaForm



def editar_categoria(request, id_categoria=None):
    if id_categoria:
        instance = Categoria.objects.get(pk=id_categoria)
    else:
        instance = None
        
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=instance)
        
        if form.is_valid():
            form.save()
            if instance:
                messages.success(request, "Editado com sucesso")
            else:
                messages.success(request, "Adicionado com sucesso")
            
            return redirect('listar_categoria')
    
    else:
        form = CategoriaForm(instance=instance)
        
    
    return render_to_response('editar_categoria.html', locals(),context_instance=RequestContext(request))
        
        
        
    
        
        
    