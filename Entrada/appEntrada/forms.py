from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Entrada(models.Model):
    id_cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, verbose_name="ID del Cliente")
    id_concierto = models.ForeignKey('Concierto', on_delete=models.CASCADE, verbose_name="ID del Concierto")
    precio = models.PositiveIntegerField(verbose_name="Precio")
    area_designada = models.CharField(max_length=50, verbose_name="Área Designada")
    fecha_reserva = models.DateField(verbose_name="Fecha de Reserva")

    def clean(self):
        # Validación de id_cliente: no puede estar vacío
        if not self.id_cliente:
            raise ValidationError({'id_cliente': "El cliente seleccionado no es válido o no existe."})

        # Validación de id_concierto: no puede estar vacío
        if not self.id_concierto:
            raise ValidationError({'id_concierto': "El concierto seleccionado no es válido o no existe."})

        # Validación de precio: debe ser mayor a 0
        if self.precio <= 0:
            raise ValidationError({'precio': "El precio debe ser un número entero positivo."})

        # Validación de área_designada: no puede estar vacío y debe tener máximo 50 caracteres
        if not self.area_designada:
            raise ValidationError({'area_designada': "El área designada es obligatoria."})
        elif len(self.area_designada) > 50:
            raise ValidationError({'area_designada': "El área designada debe tener un máximo de 50 caracteres."})

        # Validación de fecha_reserva: debe ser una fecha actual o futura
        if self.fecha_reserva < timezone.now().date():
            raise ValidationError({'fecha_reserva': "La fecha de reserva no puede ser en el pasado."})

    def save(self, *args, **kwargs):
        # Llama a las validaciones antes de guardar
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Entrada de {self.id_cliente} para {self.id_concierto} en área {self.area_designada}"
