from django.conf.urls import url, include
from .views import (home,
                    lista_pessoas,
                    lista_veiculos,
                    listaMovRot,
                    pessoa_novo,
                    veiculo_novo,
                    movrotativo_novo,
                    veiculo_update,
                    movrotativos_update,
                    pessoa_delete)

urlpatterns = [
    url(r'^$', home, name="core_home"),
    url(r"^pessoas/$", lista_pessoas, name="core_lista_pessoas"),
    url(r"^pessoas-novo/$", pessoa_novo, name="core_pessoas_novo"),
    url(r'pessoa-delete/(?P<id>\d+)/$',
        pessoa_delete, name='core_pessoa_delete'),

    url(r"^veiculos/$", lista_veiculos, name="core_lista_veiculos"),
    url(r"^veiculo-novo/$", veiculo_novo, name="core_veiculo_novo"),
    url(r'veiculo-update/(?P<id>\d+)/$',
        veiculo_update, name='core_veiculo_update'),

    url(r"^movrotativo/$", listaMovRot, name="core_lista_movrot"),
    url(r"^movrotativo-novo/$", movrotativo_novo,
        name="core_novorotativo_movrot"),
    url(r'mov_rot_update/(?P<id>\d+)/$',
        movrotativos_update, name='core_movrotativos_update')
]
