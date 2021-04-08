"""Settings for admin webapi."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


class UserAdmin(BaseUserAdmin):
    """Admin view for UserAdmin.."""

    fieldsets = (
        (None, {"fields": ("username", "email", "password", "last_login")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password1", "password2"),
            },
        ),
    )

    list_display = ("username", "email", "is_staff", "is_active", "last_login")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = (
        "username",
        "email",
    )
    ordering = (
        "username",
        "email",
    )
    filter_horizontal = ("groups", "user_permissions")


admin.site.register(User, UserAdmin)
