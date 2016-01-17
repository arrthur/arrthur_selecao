from django.conf.urls import patterns, url
from cardapio.views.index import index




urlpatterns = patterns('',
                         
    url(r'^$', index, name='index'),
)
