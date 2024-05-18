from django import forms
from .models import Project, Photo


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = '__all__'


class PhotoForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        projects = Project.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for p in projects]

        self.fields['project'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class']

