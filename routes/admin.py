from django.contrib import admin
from .models import AirportRouteNode


@admin.register(AirportRouteNode)
class AirportRouteNodeAdmin(admin.ModelAdmin):
    list_display = (
        'route_name',
        'airport_code',
        'position',
        'duration',
    )

    list_filter = (
        'route_name',
    )

    search_fields = (
        'route_name',
        'airport_code',
    )

    ordering = (
        'route_name',
        'position',
    )

    list_editable = (
        'position',
        'duration',
    )
