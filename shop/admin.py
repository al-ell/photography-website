from django.contrib import admin
from .models import Prints, PriceAndSize


class PriceAndSizeAdmin(admin.ModelAdmin):
    fields = (
        'price',
        'size',
    )


class PrintsAdmin(admin.ModelAdmin):
    fields = (
        'category',
        'name',
        'sku',
        'friendly_name',
        'description',
        'image',
        'image_url',
    )

    list_display = (
        'category',
        'name',
        'sku',
        'friendly_name',
        'description',
        'image',
        'image_url',
    )

    ordering = ('-category',)


admin.site.register(Prints, PrintsAdmin)
admin.site.register(PriceAndSize, PriceAndSizeAdmin)
