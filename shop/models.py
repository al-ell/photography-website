from django.db import models
from django.apps import apps
from projects.models import Photo, Project

class Category(models.Model):
    # Prevent plural use in Django admin
    class Meta:
        verbose_name_plural = 'Categories'
    # Import model from the projects app
    project = models.ForeignKey('projects.Project', null=True, blank=True, on_delete=models.CASCADE)


class Print(models.Model):
    class Size(models.TextChoices):
        A4 = 'A4'
        A5 = 'A5'

    # Import model from the projects app
    photo = models.ForeignKey('projects.Photo', null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    sku = models.CharField(max_length=150, null=True, blank=True)
    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sizes = models.CharField(max_length=3, choices=Size.choices, default=Size.A4)
    
    def get_friendly_name(self):
        return self.friendly_name

    
