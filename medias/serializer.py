from rest_framework.serializers import ModelSerializer
from fabrics.serializer import TinyFabricSerializer
from .models import Photo


class PhotoSerializer(ModelSerializer):

    fabric = TinyFabricSerializer(
        read_only=True,
    )

    class Meta:
        model = Photo
        fields = (
            "pk",
            "file",
            "description",
            "fabric",
        )
