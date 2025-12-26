from django.contrib import admin
from django.utils.html import format_html
from .models import Categoria, Producto, Insumo, Pedido

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("id", 
                    "nombre", 
                    "categoria", 
                    "precio", 
                    "mirar_imagen")
    
    list_filter = ("categoria",)
    search_fields = ("nombre", "descripcion")

    def mirar_imagen(self, obj):
            if obj.imagen_1:
                return format_html('<img src="{}" width="50" height="50" style="border-radius:5px;" />', obj.imagen_1.url)
            return "No hay imagen"
    mirar_imagen.short_description = "Imagen"


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre",)


@admin.register(Insumo)
class InsumoAdmin(admin.ModelAdmin):
    list_display = ("id",
                    "nombre", 
                    "tipo", 
                    "cantidad_disponible", 
                    "marca", 
                    "color")
    
    list_filter = ("tipo", "marca", "color")
    search_fields = ("nombre", "tipo", "marca", "color")


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("id", 
                    "cliente_nombre", 
                    "estado_pedido", 
                    "cliente_direccion",
                    "estado_pago", 
                    "plataforma_origen", 
                    "fecha_solicitada", 
                    "fecha_creacion")

    search_fields = ("cliente_nombre",
                    "cliente_telefono", 
                    "cliente_email",
                    "cliente_direccion", 
                    "usuario_red_social", 
                    "token_seguimiento")

    list_filter = ("estado_pedido", 
                    "estado_pago", 
                    "plataforma_origen", 
                    "fecha_creacion")
    
    readonly_fields = ("token_seguimiento", "fecha_creacion")

