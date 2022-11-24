from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    fieldsets = (
        (
            "Profile",
            {
                "fields": (
                    "username",
                    "password",
                    "avatar",
                    "name",
                    "phone",
                    "email",
                    "birth",
                    "gender",
                ),
                "classes": ("wide",),  # 필드 펴서 보기
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
                "classes": ("collapse",),  # 필드 접어서 보기
            },
        ),
        (
            "Important Dates",
            {
                "fields": ("last_login", "date_joined"),
                "classes": ("collapse",),  # 필드 접어서 보기
            },
        ),
    )

    list_display = (
        "username",
        "pk",
        "name",
        "phone",
        "email",
    )
