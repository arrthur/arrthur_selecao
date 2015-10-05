from django.conf.urls import patterns, url
from categoria.views.editar_categoria import editar_categoria
from categoria.views.listar_categoria import listar_categoria
from categoria.views.lista_categoria_serializer import Categoria_listar_serializer
from categoria.views.categoria_serializer import CategoriaSerial






urlpatterns = patterns('',
    url(r'^categoria/$', listar_categoria, name='listar_categoria'),                  
    url(r'^add_categoria/$',          editar_categoria,          name='adicionar_categoria'),               
    url(r'^categoria_serial/$',  Categoria_listar_serializer.as_view(), name='Categoria_listar_serializer'),  
    url(r'^categoria_serial/(?P<pk>[0-9]+)/$',  CategoriaSerial.as_view(), name='CategoriaSerial'),
    url(r'^editar_categoria/(?P<id_categoria>\d+)$',                           editar_categoria,          name='editar_categoria'),

)
