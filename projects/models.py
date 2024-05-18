from django.db import models


class Project(models.Model):
    # Prevent plural use in Django admin
    class Meta:
        verbose_name_plural = 'Project'

    name = models.CharField(max_length=300, null=False, blank=False)
    description = models.TextField()
    date = models.DateField(editable=True, null=False, blank=False)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name


class Photo(models.Model):
    project = models.ForeignKey('Project', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name

