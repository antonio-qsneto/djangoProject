from django.conf.urls import url, include
from .views import home, lista_pessoas, lista_veiculos, listaMovRot

urlpatterns = [
    url(r'^$', home, name="core_home"),
    url(r"^pessoas/$", lista_pessoas, name="core_lista_pessoas"),
    url(r"^veiculos/$", lista_veiculos, name="core_lista_veiculos"),
    url(r"^movrotativo/$", listaMovRot, name="core_lista_movrot")
]