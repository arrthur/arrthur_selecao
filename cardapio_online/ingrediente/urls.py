from django.conf.urls import patterns, url
from ingrediente.views.lista_ingrediente import listar_ingrediente
from ingrediente.views.editar_ingrediente import editar_ingrediente
from ingrediente.views.lista_ingrediente_serializer import Ingrediente_listar_serializer
from ingrediente.views.ingrediente_serializer import IngredienteSerial





urlpatterns = patterns('',
                       
    url(r'^ingrediente/$', listar_ingrediente, name='listar_ingrediente'),                  
    url(r'^add_ingrediente/$',          editar_ingrediente,          name='adicionar_ingrediente'),               
   url(r'^ingrediente_serial/$',  Ingrediente_listar_serializer.as_view(), name='Ingrediente_listar_serializer'), 
   url(r'^criar_ingrediente_serial/(?P<pk>[0-9]+)/$',  IngredienteSerial.as_view(), name='IngredienteSerial'),
    url(r'^editar_ingrediente/(?P<id_ingrediente>\d+)$',   editar_ingrediente,          name='editar_ingrediente'),
)
