from django.contrib import admin
from .models import Category, Prints


class CategoryAdmin(admin.ModelAdmin):
    fields = (
        'project',
    )

    ordering = ('-project',)


class PrintsAdmin(admin.ModelAdmin):
    fields = (
        'category',
        'photo', 
        'sku',
        'name',
        'friendly_name',
        'description',
        'image',
        'image_url',
        'price',
        'sizes',
    )

    list_display = (
        'category',
        'photo', 
        'sku',
        'name',
        'friendly_name',
        'description',
        'image',
        'image_url',
        'price',
        'sizes',
    )

    ordering = ('-name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Prints, PrintsAdmin)
