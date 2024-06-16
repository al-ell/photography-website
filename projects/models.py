from django.db import models


class Project(models.Model):
    """ Project Model """
    # Prevent plural use in Django admin
    class Meta:
        verbose_name_plural = 'Project'

    name = models.CharField(max_length=300, null=True, blank=True, unique=True)
    description = models.TextField(null=False, default="")

    def __str__(self):
        return self.name
    

class Photo(models.Model):
    """ photo model """
    project = models.ForeignKey(Project, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200, unique=True, default="")
    friendly_name = models.CharField(max_length=200, null=False, unique=True, default="")
    image_url = models.URLField(max_length=1024, null=False, default="")
    image = models.ImageField(null=False, default="")
    description = models.TextField(null=False, default="")

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name
