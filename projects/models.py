from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=300)
    friendly_name = models.CharField(max_length=300, null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name


class Photo(models.Model):
    project = models.ForeignKey('Project', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

