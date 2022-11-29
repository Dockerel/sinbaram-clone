from django.contrib import admin
from .models import Qna


@admin.register(Qna)
class QnaAdmin(admin.ModelAdmin):
    list_display = (
        "question",
        "pk",
        "user",
        "replied",
    )
