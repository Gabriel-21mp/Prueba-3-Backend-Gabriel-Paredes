from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InsumoViewSet, PedidoViewSet

router = DefaultRouter()
router.register(r"insumos", InsumoViewSet, basename="insumos")
router.register(r"pedidos", PedidoViewSet, basename="pedidos")

urlpatterns = [
    path("", include(router.urls)),
]


