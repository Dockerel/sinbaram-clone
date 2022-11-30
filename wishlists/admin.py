from django.contrib import admin
from .models import Wishlist


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "pk",
        "user",
        "created_at",
        "updated_at",
    )
