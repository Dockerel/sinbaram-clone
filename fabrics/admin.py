from django.contrib import admin
from .models import Fabric


@admin.register(Fabric)
class FabricAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "pk",
        "code",
        "color",
        "price",
        "kind",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "color",
        "kind",
    )
