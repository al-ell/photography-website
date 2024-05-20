from django.contrib import admin
from .models import Category, Print


class CategoryAdmin(admin.ModelAdmin):
    fields = (
        'project',
    )

    ordering = ('-project',)


class PrintAdmin(admin.ModelAdmin):
    fields = (
        'photo', 
        'category',
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
        'photo', 
        'category',
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
admin.site.register(Print, PrintAdmin)
