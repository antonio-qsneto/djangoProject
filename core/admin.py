from django.contrib import admin
from .models import Pessoa, Marca, Veiculo, Parametros, MovRotativo, Mensalista, MovMensalista, VagaReservada


class MovRotativoAdm(admin.ModelAdmin):
    list_display = ('checkin', 'checkout', 'valor_hora',
                    'pago', 'total', 'horas_total', 'veiculo')


class MovMensalistaAdm(admin.ModelAdmin):
    list_display = ('mensalista', 'data_pag', 'total')


admin.site.register(Pessoa)
admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Parametros)
admin.site.register(Mensalista)
admin.site.register(VagaReservada)
admin.site.register(MovMensalista, MovMensalistaAdm)
admin.site.register(MovRotativo, MovRotativoAdm)
