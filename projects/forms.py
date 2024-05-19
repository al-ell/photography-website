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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    class Meta:
        model = Photo
        fields = '__all__'

    

