from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^cadastros/moeda_list', views.moeda_list, name="moeda_list"),
    url(r'^cadastros/', views.cadastros, name="cadastros"),
    url(r'^pedidos/', views.pedidos, name="pedidos"),
]
