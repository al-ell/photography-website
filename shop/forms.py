from django import forms
from .widgets import CustomClearableFileInput
from crispy_forms.helper import FormHelper
from .models import Prints, PriceAndSize



class PriceAndSizeForm(forms.ModelForm):

    class Meta:
        model = PriceAndSize
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)


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
        ]

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        


    

    

