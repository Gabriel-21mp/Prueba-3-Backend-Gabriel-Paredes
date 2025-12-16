from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = [
            'cliente_nombre',
            'cliente_email',
            'cliente_telefono',
            'usuario_red_social',
            'cliente_direccion',
            'descripcion',
            'fecha_solicitada',
            'imagen_referencia'
        ]

        widgets = {
            'fecha_solicitada': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'cliente_nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'cliente_email': forms.EmailInput(attrs={'class': 'form-control'}),
        }