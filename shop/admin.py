from django.contrib import admin
from .models import Prints, Category


class CategoryAdmin(admin.ModelAdmin):
    """ Category admin """
    fields = ('name',)

    list_display = ('name',)


class PrintsAdmin(admin.ModelAdmin):
    """ Prints admin """
    fields = (
        'category',
        'name',
        'sku',
        'friendly_name',
        'description',
        'limited_edition',
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
        'limited_edition',
        'image',
        'image_url',
        'a4_price',
        'a5_price',
    )

    ordering = ('-category',)


admin.site.register(Prints, PrintsAdmin)
admin.site.register(Category, CategoryAdmin)
