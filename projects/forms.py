from django import forms
from crispy_forms.helper import FormHelper
from .models import Project, Photo
from datetime import datetime


class DateInput(forms.DateInput):
        input_type = 'date'


class ProjectForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    class Meta:
        model = Project
        fields = ['name', 'description', 'date',]

    placeholders = {
        'name': 'Project Name',
        'description': 'Description',
        'date': 'Date',
    }
    
    widgets = {
        'date': DateInput(),
    }

    

class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ['project', 'name', 'friendly_name', 'image_url', 'description',]

    image = forms.ImageField(label='Image', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        projects = Project.objects.all()


    placeholders = {
        'project': 'Project',
        'name': 'Name',
        'friendly_name': 'Public Name',
        'description': 'Description',
    }

    

