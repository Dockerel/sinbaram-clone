from rest_framework.serializers import SerializerMethodField
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

    rating = SerializerMethodField()

    class Meta:
        model = Fabric
        fields = "__all__"

    def get_rating(self, fabric):
        return fabric.rating()


class TinyFabricSerializer(ModelSerializer):
    class Meta:
        model = Fabric
        fields = (
            "pk",
            "name",
            "code",
            "kind",
        )
