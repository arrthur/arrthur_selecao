'''
Created on 16/01/2016

@author: Arthur
'''
from django.contrib.auth import logout
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def logout_acesso(request):
    logout(request)
    return render_to_response('index.html', locals(),context_instance=RequestContext(request))
    