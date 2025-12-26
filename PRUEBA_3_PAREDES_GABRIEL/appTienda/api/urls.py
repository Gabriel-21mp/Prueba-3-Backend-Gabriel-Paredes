# appTienda/api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InsumoViewSet, PedidoViewSet, PedidoFiltrarAPIView

router = DefaultRouter()
router.register(r"insumos", InsumoViewSet, basename="insumo")
router.register(r"pedidos", PedidoViewSet, basename="pedido")

urlpatterns = [
    path("pedidos/filtrar/", PedidoFiltrarAPIView.as_view(), name="pedido_filtrar"),
    path("", include(router.urls)),
]
