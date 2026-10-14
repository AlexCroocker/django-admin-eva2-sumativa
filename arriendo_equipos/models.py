from django.db import models

class Equipo(models.Model):
    id_equipo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    precio_arriendo = models.IntegerField()
    stock = models.BooleanField()
    descripcion = models.TextField(blank=True)
    monto_valor = models.IntegerField()

    def __str__(self):
        return self.nombre

class Arriendo(models.Model):
    id_equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    hora_arriendo = models.TimeField()
    fecha_arriendo = models.DateField()
    fecha_devolucion = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=[('pendiente', 'Pendiente'), ('devuelto', 'Devuelto')], default='pendiente')
    monto_valor = models.IntegerField()