from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Answer
from qnas.serializer import QnaSerializer


class AnswerSerializer(ModelSerializer):

    question = QnaSerializer(
        read_only=True,
    )

    is_replied = serializers.SerializerMethodField()

    class Meta:
        model = Answer
        fields = (
            "pk",
            "question",
            "answer",
            "is_replied",
        )

    def get_is_replied(self, answer):
        return True
