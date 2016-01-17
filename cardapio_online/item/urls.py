from django.conf.urls import patterns, url
from item.views.lista_item import lista_item
from item.views.lista_item_serializer import Lista_item_serializer,\
    Criar_item_serializer
from item.views.editar_item import editar_item
from item.views.item_serializer import ItemSerial
from item.views.remover_item import remover_item




urlpatterns = patterns('',
                       
     url(r'^itens/$', lista_item, name='lista_item'),
     url(r'^listar_itens_serial/$',  Lista_item_serializer.as_view(), name='Lista_item_serializer'),
     url(r'^criar_itens_serial/$',  Criar_item_serializer.as_view(), name='Criar_item_serializer'),
     url(r'^item_serial/(?P<pk>[0-9]+)/$',  ItemSerial.as_view(), name='ItemSerial'),
     
     url(r'^add_item/$',          editar_item,          name='adicionar_item'),
     url(r'^editar_item/(?P<id_item>\d+)$', editar_item, name='editar_item'),
     url(r'^remover_item/(?P<id_item>\d+)$', remover_item, name='remover_item')

)
