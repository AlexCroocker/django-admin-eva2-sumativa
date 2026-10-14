from types import SimpleNamespace
from datetime import date, time

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .admin import ArriendoAdmin, EquipoAdmin
from .models import Arriendo, Equipo


class MontosAdminTests(TestCase):
    def test_listados_usan_columnas_monetarias_formateadas(self):
        self.assertIn('precio_arriendo_pesos', EquipoAdmin.list_display)
        self.assertIn('monto_valor_pesos', EquipoAdmin.list_display)
        self.assertIn('monto_valor_pesos', ArriendoAdmin.list_display)

    def test_equipo_muestra_precios_en_pesos_chilenos(self):
        equipo = SimpleNamespace(precio_arriendo=12990, monto_valor=1250000)
        equipo_admin = EquipoAdmin(Equipo, admin.site)

        self.assertEqual(str(equipo_admin.precio_arriendo_pesos(equipo)), '<strong>$12.990</strong>')
        self.assertEqual(str(equipo_admin.monto_valor_pesos(equipo)), '<strong>$1.250.000</strong>')

    def test_arriendo_muestra_monto_en_pesos_chilenos(self):
        arriendo = SimpleNamespace(monto_valor=12990)
        arriendo_admin = ArriendoAdmin(Arriendo, admin.site)

        self.assertEqual(str(arriendo_admin.monto_valor_pesos(arriendo)), '<strong>$12.990</strong>')

    def test_listado_de_equipos_muestra_todos_los_montos_con_separador(self):
        usuario = get_user_model().objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='test-password',
        )
        self.client.force_login(usuario)
        Equipo.objects.create(
            nombre='Equipo prueba',
            precio_arriendo=100000,
            stock=True,
            descripcion='',
            monto_valor=100000,
        )

        respuesta = self.client.get(reverse('admin:arriendo_equipos_equipo_changelist'))

        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, '<strong>$100.000</strong>', html=True, count=2)

    def test_listado_de_arriendos_muestra_monto_con_separador(self):
        usuario = get_user_model().objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='test-password',
        )
        self.client.force_login(usuario)
        equipo = Equipo.objects.create(
            nombre='Equipo prueba',
            precio_arriendo=100000,
            stock=True,
            descripcion='',
            monto_valor=100000,
        )
        Arriendo.objects.create(
            id_equipo=equipo,
            hora_arriendo=time(10, 0),
            fecha_arriendo=date(2026, 10, 14),
            monto_valor=100000,
        )

        respuesta = self.client.get(reverse('admin:arriendo_equipos_arriendo_changelist'))

        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, '<strong>$100.000</strong>', html=True)
