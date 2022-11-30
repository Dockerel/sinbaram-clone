from rest_framework.serializers import ModelSerializer
from .models import Wishlist
from fabrics.serializer import TinyFabricSerializer


class WishlistSerializer(ModelSerializer):

    fabrics = TinyFabricSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Wishlist
        fields = (
            "pk",
            "name",
            "fabrics",
        )
