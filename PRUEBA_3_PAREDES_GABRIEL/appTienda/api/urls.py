from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InsumoViewSet, PedidoViewSet, PedidoFiltrarAPIView


router = DefaultRouter()
router.register(r"insumos", InsumoViewSet, basename="insumos")
router.register(r"pedidos", PedidoViewSet, basename="pedidos")


urlpatterns = [
    path("pedidos/filtrar/", PedidoFiltrarAPIView.as_view(), name="api_pedidos_filtrar"),
    path("", include(router.urls)),
]


