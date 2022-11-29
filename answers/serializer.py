from rest_framework.serializers import ModelSerializer
from .models import Answer
from qnas.serializer import QnaSerializer


class AnswerSerializer(ModelSerializer):

    question = QnaSerializer(
        read_only=True,
    )

    class Meta:
        model = Answer
        fields = (
            "pk",
            "question",
            "answer",
        )
