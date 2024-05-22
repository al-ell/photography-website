from django.db import models
from django.apps import apps
from projects.models import Photo, Project


class Prints(models.Model):
    class Meta:
        verbose_name_plural = 'Prints'

    class Size(models.TextChoices):
        A4 = 'A4'
        A5 = 'A5'

    # Import model from the projects app
    category = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.ForeignKey(Photo, on_delete=models.CASCADE)
    sku = models.CharField(max_length=150, null=True, blank=True)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sizes = models.CharField(max_length=3, choices=Size.choices, default=Size.A4)
    
    def __str__(self):
        return self.name, self.category, self.image
    
    def get_friendly_name(self):
        return self.friendly_name

    
