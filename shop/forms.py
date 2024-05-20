from django import forms
from crispy_forms.helper import FormHelper
from .models import Category, Prints
   

class PrintsForm(forms.ModelForm):

    class Meta:
        model = Prints
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        categories = Category.objects.all()
        


    

    

