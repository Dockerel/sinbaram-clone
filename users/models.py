from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    """User Model Definition"""

    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")

    avatar = models.URLField(
        blank=True,
        null=True,
    )
    name = models.CharField(
        max_length=150,
    )
    phone = models.CharField(
        max_length=11,
        default="",
    )
    email = models.CharField(
        max_length=150,
        default="",
    )
    birth = models.CharField(
        max_length=6,
        default="",
    )
    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
    )
