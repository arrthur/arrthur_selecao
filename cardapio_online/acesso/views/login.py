# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.contrib import auth


def login(request):

    if request.POST:
        username = request.POST.get('usuario')
        password = request.POST.get('pass')
        
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index_acesso')
    
        else:
            error_message = 'Usuário ou senha incorreto(s).'



    return render_to_response('login1.html', locals(), 
                              context_instance=RequestContext(request))
    
def index_acesso(request):
    return render_to_response('index_acesso.html', locals(), 
                              context_instance=RequestContext(request))