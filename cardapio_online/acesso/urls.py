from django.conf.urls import patterns, url
from cardapio.views.index import index
from acesso.views.login import login, index_acesso
from item.views.lista_item import listar_item_acesso




urlpatterns = patterns('',
     url(r'^login/$', login, name='login'),
     url(r'^index/$', index_acesso, name='index_acesso'),
     url(r'^itens_acesso/$', listar_item_acesso, name='listar_item_acesso'),

)
