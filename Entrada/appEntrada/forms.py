from django import forms
from appCliente.models import cliente  # Importa correctamente el modelo Cliente desde appCliente
from appConcierto.models import Concierto  # Importa correctamente el modelo Concierto desde appConcierto
from appEntrada.models import Entrada  # Asumiendo que Entrada es el modelo de la tabla en appEntrada

class FormEntrada(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ['id_cliente', 'id_concierto', 'precio', 'area_designada', 'fecha_reserva']