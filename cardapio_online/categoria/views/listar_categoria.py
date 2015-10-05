# -*- coding: utf-8 -*-
from categoria.models.categoria import Categoria
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def listar_categoria(request):
    categorias = Categoria.objects.all().order_by('id')
    
    try:
        pesquisa = request.GET.get('buscar_categoria').strip().upper()
    except:
        pesquisa = ''

    if pesquisa:
        categorias = Categoria.objects.filter(nome__icontains = pesquisa).order_by('id')
        
   
    
    return render_to_response('listar_categoria.html',locals(),context_instance=RequestContext(request))
    