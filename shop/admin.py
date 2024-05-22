from django.contrib import admin
from .models import Prints


class PrintsAdmin(admin.ModelAdmin):
    fields = (
        'category',
        'name',
        'sku',
        'friendly_name',
        'description',
        'image',
        'image_url',
        'price',
        'sizes',
    )

    list_display = (
        'category',
        'name',
        'sku',
        'friendly_name',
        'description',
        'image',
        'image_url',
        'price',
        'sizes',
    )

    ordering = ('-category',)


admin.site.register(Prints, PrintsAdmin)
