from django.conf.urls import patterns, include, url
from django.contrib import admin
from cardapio.views.index import index
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^cardapio/', include('cardapio.urls')),
    url(r'^categoria/', include('categoria.urls')),
    url(r'^ingrediente/', include('ingrediente.urls')),
    url(r'^item/', include('item.urls')),
    url(r'^acesso/', include('acesso.urls')),
    url(r'^$', index, name='index'),
    
    

    url(r'^admin/', include(admin.site.urls)), #Criacao de usuarios e grupos
)