from django.db import models
from common.models import CommonModel


class Fabric(CommonModel):

    """Fabric Model Definition"""

    class FabricKindChoices(models.TextChoices):
        PLAIN_FABRIC = ("plain_fabric", "Plain Fabric")
        LINEN_FABRIC = ("linen_fabric", "Linen Fabric")

    name = models.CharField(
        max_length=180,
        default="",
    )
    code = models.CharField(
        max_length=10,
        default="",
    )
    color = models.TextField(
        max_length=180,
        default="",
    )
    price = models.PositiveIntegerField()
    kind = models.CharField(
        max_length=20,
        choices=FabricKindChoices.choices,
    )

    def __str__(self):
        return self.name

    def rating(fabric):
        count = fabric.reviews.count()
        if count == 0:
            return 0
        else:
            total_rating = 0
            for review in fabric.reviews.all().values("rating"):
                total_rating += review["rating"]
            return round(total_rating / count, 2)
