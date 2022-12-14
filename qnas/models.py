from django.db import models
from common.models import CommonModel


class Qna(CommonModel):

    """Qna Model Definition"""

    fabric = models.ForeignKey(
        "fabrics.Fabric",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="qnas",
    )
    question = models.CharField(
        max_length=1000,
    )
    user = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="qnas",
    )

    def __str__(self):
        return f"[{str(self.pk)}] - " + self.question[:15] + "..."
