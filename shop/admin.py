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
        'a4_price',
        'a5_price',
    )

    list_display = (
        'category',
        'name',
        'sku',
        'friendly_name',
        'description',
        'image',
        'image_url',
        'a4_price',
        'a5_price',
    )

    ordering = ('-category',)


admin.site.register(Prints, PrintsAdmin)

