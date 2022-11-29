from rest_framework.serializers import ModelSerializer
from .models import Qna
from users.serializer import TinyUserSerializer
from fabrics.serializer import TinyFabricSerializer


class QnaSerializer(ModelSerializer):

    user = TinyUserSerializer(
        read_only=True,
    )

    class Meta:
        model = Qna
        fields = (
            "pk",
            "question",
            "user",
        )


class NewQnaSerializer(ModelSerializer):
    class Meta:
        model = Qna
        fields = (
            "question",
            "fabric",
        )


class QnaDetailSerializer(ModelSerializer):

    user = TinyUserSerializer(
        read_only=True,
    )
    fabric = TinyFabricSerializer(
        read_only=True,
    )

    class Meta:
        model = Qna
        fields = "__all__"
