from django.contrib import admin
from django.utils.html import format_html
from .models import Equipo, Arriendo


def _formatear_pesos_chilenos(monto):
    signo = "-$" if monto < 0 else "$"
    monto_formateado = f"{signo}{abs(monto):,}".replace(",", ".")
    return format_html('<strong>{}</strong>', monto_formateado)


class EquipoAdmin(admin.ModelAdmin):
    list_display = (
        'id_equipo',
        'nombre',
        'precio_arriendo_pesos',
        'stock',
        'descripcion',
        'monto_valor_pesos',
    )
    search_fields = ('nombre',)
    list_filter = ('stock',)

    @admin.display(description='Precio arriendo', ordering='precio_arriendo')
    def precio_arriendo_pesos(self, obj):
        return _formatear_pesos_chilenos(obj.precio_arriendo)

    @admin.display(description='Monto valor', ordering='monto_valor')
    def monto_valor_pesos(self, obj):
        return _formatear_pesos_chilenos(obj.monto_valor)


class ArriendoAdmin(admin.ModelAdmin):
    list_display = (
        'id_equipo',
        'hora_arriendo',
        'fecha_arriendo',
        'fecha_devolucion',
        'estado',
        'monto_valor_pesos',
    )
    search_fields = ('id_equipo__nombre',)
    list_filter = ('estado',)

    @admin.display(description='Monto valor', ordering='monto_valor')
    def monto_valor_pesos(self, obj):
        return _formatear_pesos_chilenos(obj.monto_valor)


admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Arriendo, ArriendoAdmin)