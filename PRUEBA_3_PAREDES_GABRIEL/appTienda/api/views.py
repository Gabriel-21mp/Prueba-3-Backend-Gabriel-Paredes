from rest_framework import viewsets, status
from rest_framework.response import Response
from appTienda.models import Insumo, Pedido
from .serializers import InsumoSerializer
from .serializers import PedidoSerializer

class InsumoViewSet(viewsets.ModelViewSet):
    queryset = Insumo.objects.all().order_by("id")
    serializer_class = InsumoSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all().order_by("-id")
    serializer_class = PedidoSerializer
    
    def list(self, request, *args, **kwargs):
        return Response(
            {"detail": "Listado no permitido en este endpoint."},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )
    
    def destroy(self, request, *args, **kwargs):
        return Response(
            {"detail": "Eliminación no permitida en este endpoint."},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )
