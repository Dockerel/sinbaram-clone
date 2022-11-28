from rest_framework.serializers import ModelSerializer
from .models import Qna


class QnaSerializer(ModelSerializer):
    class Meta:
        model = Qna
        fields = (
            "pk",
            "question",
        )


class NewQnaSerializer(ModelSerializer):
    class Meta:
        model = Qna
        fields = (
            "question",
            "fabric",
        )
