from django import forms
from crispy_forms.helper import FormHelper
from .models import Project, Photo


class ProjectForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    class Meta:
        model = Project
        fields = '__all__'

    placeholders = {
        'name': 'Project Name',
        'description': 'Description',
        'date': 'Date',
    }

    class DateInput(forms.DateInput):
        input_type = 'date'
    
    date_input = forms.DateField(widget=DateInput)

class PhotoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    class Meta:
        model = Photo
        fields = '__all__'

    

