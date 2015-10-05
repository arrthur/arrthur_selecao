# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from ingrediente.models.ingrediente import Ingrediente


def listar_ingrediente(request):
    ingredientes = Ingrediente.objects.all().order_by('id')
    
    try:
        pesquisa = request.GET.get('buscar_ingrediente').strip().upper()
    except:
        pesquisa = ''

    if pesquisa:
        ingredientes = Ingrediente.objects.filter(nome__icontains = pesquisa).order_by('id')
        
   
    
    return render_to_response('listar_ingrediente.html',locals(),context_instance=RequestContext(request))
    