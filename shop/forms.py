from django import forms
from .widgets import CustomClearableFileInput
from crispy_forms.helper import FormHelper
from .models import Prints


class PrintsForm(forms.ModelForm):

    class Meta:
        model = Prints
        fields = [
            'category',
            'name',
            'sku',
            'friendly_name',
            'image_url',
            'image',
            'description',
            'a5_price',
            'a4_price',
        ]

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        


    

    

