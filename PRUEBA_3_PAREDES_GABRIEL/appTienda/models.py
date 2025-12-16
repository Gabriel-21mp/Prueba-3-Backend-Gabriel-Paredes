from django.db import models
from django.utils.crypto import get_random_string
from django.core.exceptions import ValidationError


PLATAFORMAS = (
    ('FACEBOOK', 'Facebook'),
    ('INSTAGRAM', 'Instagram'),
    ('WHATSAPP', 'WhatsApp'),
    ('PRESENCIAL', 'Presencial'),
    ('SITIO_WEB', 'Sitio Web')
)

ESTADOS = (
    ('SOLICITADO', 'Solicitado'),
    ('APROBADO','Aprobado'),
    ('EN_PROCESO', 'En Proceso'),
    ('REALIZADO','Realizado'),
    ('ENTREGADO','Entregado'),
    ('FINALIZADO','Finalizado'),
    ('CANCELADO','Cancelado')
)

ESTADOS_PAGO = (
    ('PENDIENTE', 'Pendiente'), 
    ('PAGADO', 'Pagado'),
    ('PARCIAL','Parcial')
)


class Categoria(models.Model):
    nombre = models.CharField(max_length=125)
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=125)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen_1 = models.ImageField(upload_to='productos/', blank=True, null=True)
    imagen_2 = models.ImageField(upload_to='productos/', blank=True, null=True)
    imagen_3 = models.ImageField(upload_to='productos/', blank=True, null=True)

class Insumo(models.Model):
    nombre = models.CharField(max_length=125)
    tipo = models.CharField(max_length=100)
    cantidad_disponible = models.IntegerField()
    marca = models.CharField(max_length=100)
    color = models.CharField(max_length=50)



class Pedido(models.Model):
    cliente_nombre = models.CharField(max_length=125)
    cliente_direccion = models.CharField(max_length=255, blank=True, null=True)
    cliente_telefono = models.CharField(max_length=20)
    cliente_email = models.EmailField(blank=True, null=True)
    usuario_red_social = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField()
    fecha_solicitada = models.DateField(blank=True, null=True)
#clientes^

    producto_referencia = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True, blank=True)
    plataforma_origen = models.CharField(max_length=20, choices=PLATAFORMAS, default='SITIO_WEB')
    estado_pedido = models.CharField(max_length=20, choices=ESTADOS, default='SOLICITADO')
    estado_pago = models.CharField(max_length=20, choices=ESTADOS_PAGO, default='PENDIENTE')
#pagos y plataforma^
    imagen_referencia = models.ImageField(upload_to='pedidos/', blank=True, null=True)
#imagenes^
    token_seguimiento = models.CharField(max_length=32, unique=True, editable=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
#fecha y token^
    def save(self, *args, **kwargs):
        if not self.token_seguimiento:
            self.token_seguimiento = get_random_string(24)
        super().save(*args, **kwargs)

    def clean(self):
        if self.estado_pedido == 'FINALIZADO' and self.estado_pago != 'PAGADO':
            raise ValidationError(
                "No se puede finalizar un pedido si el pago no está completo"
            )

    def __str__(self):
        return f"Pedido #{self.id} - {self.cliente_nombre}"
