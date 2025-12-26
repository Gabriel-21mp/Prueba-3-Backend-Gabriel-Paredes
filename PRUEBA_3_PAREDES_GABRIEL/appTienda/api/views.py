from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.utils.dateparse import parse_date
from appTienda.models import Insumo, Pedido
from .serializers import InsumoSerializer, PedidoSerializer

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


class PedidoFiltrarAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        desde = request.GET.get("desde")
        hasta = request.GET.get("hasta")
        estados = request.GET.getlist("estado")
        limit = request.GET.get("limit", "50")
        try:
            limit = int(limit)
            if limit < 1 or limit > 200:
                return Response({"error": "limit debe estar entre 1 y 200"}, status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response({"error": "limit debe ser un número"}, status=status.HTTP_400_BAD_REQUEST)
        qs = Pedido.objects.all().order_by("-fecha_creacion")
        if desde:
            d = parse_date(desde)
            if not d:
                return Response({"error": "desde debe tener formato YYYY-MM-DD"}, status=status.HTTP_400_BAD_REQUEST)
            qs = qs.filter(fecha_creacion__date__gte=d)
        if hasta:
            h = parse_date(hasta)
            if not h:
                return Response({"error": "hasta debe tener formato YYYY-MM-DD"}, status=status.HTTP_400_BAD_REQUEST)
            qs = qs.filter(fecha_creacion__date__lte=h)
        if estados:
            estados_validos = [e[0] for e in Pedido._meta.get_field("estado_pedido").choices]
            for e in estados:
                if e not in estados_validos:
                    return Response({"error": f"estado inválido: {e}", "validos": estados_validos}, status=status.HTTP_400_BAD_REQUEST)
            qs = qs.filter(estado_pedido__in=estados)
        qs = qs[:limit]
        data = PedidoSerializer(qs, many=True).data
        return Response({"count": len(data), "results": data}, status=status.HTTP_200_OK)
