from django.db import models
from appCliente.models import Cliente
from appConcierto.models import Concierto
# Create your models here.

class Entrada(models.Model):
    id_entrada = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_concierto = models.ForeignKey(Concierto, on_delete=models.CASCADE)
    precio = models.IntegerField()
    area_designada = models.CharField(max_length=50)
    fecha_reserva = models.DateField()
