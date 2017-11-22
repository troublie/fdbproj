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
    url(r'^pedidos/remove/(?P<pk>\d+)/$', views.pedidos_remove, name="pedidos_remove"),
    url(r'^pedidos/edit/(?P<pk>\d+)/$', views.pedidos_edit, name="pedidos_edit"),
    url(r'^pedidos/detail/(?P<pk>\d+)/$', views.pedidos_detail, name="pedidos_detail"),
    url(r'^pedidos/new', views.pedidos_new, name="pedidos_new"),
    url(r'^pedidos/list', views.pedidos_list, name="pedidos_list"),
    url(r'^pedidos/', views.pedidos, name="pedidos"),
]
