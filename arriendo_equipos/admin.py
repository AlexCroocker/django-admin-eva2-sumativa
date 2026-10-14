from django.contrib import admin
from .models import Equipo, Arriendo

class EquipoAdmin(admin.ModelAdmin):
    list_display = ('id_equipo', 'nombre', 'precio_arriendo', 'stock', 'descripcion', 'monto_valor')
    search_fields = ('nombre',)
    list_filter = ('stock',)

class ArriendoAdmin(admin.ModelAdmin):
    list_display = ('id_equipo', 'hora_arriendo', 'fecha_arriendo', 'fecha_devolucion', 'estado', 'monto_valor')
    search_fields = ('id_equipo__nombre',)
    list_filter = ('estado',)

admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Arriendo, ArriendoAdmin)