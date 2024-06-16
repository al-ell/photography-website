from django.contrib import admin
from .models import Project, Photo


class ProjectAdmin(admin.ModelAdmin):
    """ Project Admin """
    fields = (
        'name',
        'description',
    )

    list_display = (
        'name',
        'description',

    )

    ordering = ('-name',)


class PhotoAdmin(admin.ModelAdmin):
    """ Photo admin """
    fields = (
        'project',
        'name',
        'friendly_name',
        'description',
        'image',
        'image_url',
    )

    list_display = (
        'project',
        'friendly_name',
        'description',
        'image',
    )

    ordering = ('name',)


admin.site.register(Project, ProjectAdmin)
admin.site.register(Photo, PhotoAdmin)
