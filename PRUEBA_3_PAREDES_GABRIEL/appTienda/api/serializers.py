from rest_framework import serializers
from appTienda.models import Insumo
from appTienda.models import Pedido



class InsumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insumo
        fields = "__all__"


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = "__all__"
        read_only_fields = ("token_seguimiento", "fecha_creacion")
