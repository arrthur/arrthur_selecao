# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from item.models.item import Item
from categoria.models.categoria import Categoria


def lista_item(request):
    itens = Item.objects.all()
    categorias = Categoria.objects.all()
    
    try:
        buscar_item = request.GET.get('buscar_item').strip().upper()
        buscar_categoria = request.GET.get('buscar_categoria')
        
    except:
        buscar_item = ''
        buscar_categoria = ''
        
        
    
        
    if buscar_item:
        itens = Item.objects.filter(nome__icontains = buscar_item)
        
    if buscar_categoria:
        itens = Item.objects.filter(categoria__id = buscar_categoria)
    
        
    

    return render_to_response('lista_item.html',locals(),context_instance=RequestContext(request))


def listar_item_acesso(request):
    itens = Item.objects.all()
    categorias = Categoria.objects.all()
    
    try:
        buscar_item = request.GET.get('buscar_item').strip().upper()
        buscar_categoria = request.GET.get('buscar_categoria')
        
    except:
        buscar_item = ''
        buscar_categoria = ''
        
        
    
        
    if buscar_item:
        itens = Item.objects.filter(nome__icontains = buscar_item)
        
    if buscar_categoria:
        itens = Item.objects.filter(categoria__id = buscar_categoria)
    
        
    

    return render_to_response('listar_item_acesso.html',locals(),context_instance=RequestContext(request))
    


