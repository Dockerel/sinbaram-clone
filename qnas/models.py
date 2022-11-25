from django.db import models
from common.models import CommonModel


class Qna(CommonModel):

    """Q&A Model Definition"""

    question = models.TextField(
        max_length=1000,
    )
    user = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    answer = models.TextField(
        max_length=1000,
        null=True,
        blank=True,
    )
