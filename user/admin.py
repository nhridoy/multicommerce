from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


# Register your models here.

class AdminUser(UserAdmin):
    ordering = ("-date_joined",)
    search_fields = (
        "username",
        "email",
    )
    list_filter = (
        "is_active",
        "is_staff",
        "is_superuser",
        "user_type",
    )
    list_display = (
        "username",
        "email",
        "user_type",
        "date_joined",
        "is_active",
    )
    fieldsets = (
        (
            "Login Info",
            {
                "fields": (
                    "username",
                    "email",
                    "password",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "user_type",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "user_type",
                    "password1",
                    "password2",
                ),
            },
        ),
    )


admin.site.register(User, AdminUser)
