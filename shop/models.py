from django.db import models
from projects.models import Photo, Project


class Category(models.Model):
    """ Category model """
    class Meta:
        verbose_name_plural = 'Categories'

    # Import model from the projects app
    name = models.ForeignKey(Project, blank=False,
                             null=False, default="", on_delete=models.PROTECT)
    def __str__(self):
        return self.name.name

class Prints(models.Model):
    """ Prints model """
    class Meta:
        verbose_name_plural = 'Prints'
    # import from category model
    category = models.ForeignKey(Category, null=False, blank=False,
                                default="", on_delete=models.PROTECT)
    # Import model from the projects app
    name = models.ForeignKey(Photo, null=False, blank=False,
                             default="", on_delete=models.PROTECT)
    sku = models.CharField(max_length=150, null=False,
                           unique=True, default="00", blank=False)
    friendly_name = models.CharField(max_length=200, default="", unique=True, blank=False)
    image_url = models.URLField(max_length=1024, default="", unique=True)
    image = models.ImageField(default="")
    description = models.TextField(null=False, default="", blank=False)
    has_sizes = models.BooleanField(default=True)
    limited_edition = models.BooleanField(default=False, null=False, blank=False)
    a4_price = models.DecimalField(max_digits=6, decimal_places=2,
                                    default=120.00, blank=False)
    a5_price = models.DecimalField(max_digits=6, decimal_places=2,
                                    default=80.00, blank=False)

    # Return price options for different sizes
    def get_price_options(self):
        return [
            ('A5', self.a5_price),
            ('A4', self.a4_price),
        ]

    def __str__(self):
        return self.name.name

    def get_friendly_name(self):
        return self.friendly_name
