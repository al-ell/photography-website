from django.contrib import admin
from .models import Project, Photo


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'date',
    )


class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        'project',
        'name',
        'friendly_name',
        'description',
        'image',
    )

    ordering = ('name',)


admin.site.register(Project, ProjectAdmin)
admin.site.register(Photo, PhotoAdmin)
