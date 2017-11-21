from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^cadastros/cliente/list', views.cliente_list, name="cliente_list"),
    url(r'^cadastros/moeda/list', views.moeda_list, name="moeda_list"),
    url(r'^cadastros/termo/new/$', views.termo_new, name="termo_new"),
    url(r'^cadastros/termo/list', views.termo_list, name="termo_list"),
    url(r'^cadastros/termo/detalhe/(?P<pk>\d+)/$', views.termo_detail, name="termo_detail"),
    url(r'^cadastros/termo/edit/(?P<pk>\d+)/$', views.termo_edit, name="termo_edit"),
    url(r'^cadastros/termo/remove/(?P<pk>\d+)/$', views.termo_remove, name="termo_remove"),
    url(r'^cadastros/', views.cadastros, name="cadastros"),
    url(r'^pedidos/list', views.pedidos_list, name="pedidos_list"),
    url(r'^pedidos/', views.pedidos, name="pedidos"),
]
