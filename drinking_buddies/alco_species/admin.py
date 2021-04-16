"""Settings for admin webapi."""
from django.contrib import admin

from .models import AlcoholGroup, AlcoholType


class AlcoholTypeAdmin(admin.ModelAdmin):
    """Admin view for AlcoholType."""

    ordering = ["name", "description"]
    list_display = ["name", "description", "groups"]
    list_filter = ["name"]


class AlcoholGroupAdmin(admin.ModelAdmin):
    """Admin view for AlcoholGroup."""

    model = AlcoholGroup

    ordering = ["name"]
    list_display = ["name", "parent", "type"]
    list_filter = ["type", "parent", "name"]


admin.site.register(AlcoholType, AlcoholTypeAdmin)
admin.site.register(AlcoholGroup, AlcoholGroupAdmin)
