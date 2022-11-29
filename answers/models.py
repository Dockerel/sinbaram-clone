from django.db import models
from common.models import CommonModel


class Answer(CommonModel):

    """Answer Model Definition"""

    answer = models.CharField(
        max_length=1000,
    )
    question = models.OneToOneField(
        "qnas.Qna",
        on_delete=models.CASCADE,
        related_name="answers",
    )

    def __str__(self):
        return f"[{str(self.pk)}] - " + self.answer[:15] + "..."
