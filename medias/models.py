from django.db import models
from common.models import CommonModel


class Photo(CommonModel):

    """Photo Model Definition"""

    file = models.URLField()
    description = models.CharField(
        max_length=140,
    )
    fabric = models.ForeignKey(
        "fabrics.Fabric",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="photos",
    )
