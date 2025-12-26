from django.urls import path
from . import views

urlpatterns = [
    path("", views.catalogo, name="catalogo"),
    path("producto/<int:id>/", views.detalle_producto, name="detalle_producto"),
    path("solicitud/", views.solicitud_pedido, name="solicitud_pedido"),
    path("seguimiento/<str:token>/", views.detalle_seguimiento, name="detalle_seguimiento"),
    path("reporte/", views.reporte_pedidos, name="reporte_pedidos"),
]
