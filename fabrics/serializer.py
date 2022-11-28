from rest_framework.serializers import ModelSerializer
from .models import Fabric


class FabricSerializer(ModelSerializer):
    class Meta:
        model = Fabric
        fields = (
            "pk",
            "name",
            "code",
            "price",
            "kind",
        )


class FabricDetailSerializer(ModelSerializer):
    class Meta:
        model = Fabric
        fields = "__all__"


class TinyFabricSerializer(ModelSerializer):
    class Meta:
        model = Fabric
        fields = (
            "pk",
            "name",
            "code",
            "kind",
        )
