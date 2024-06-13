from django import forms
from .widgets import CustomClearableFileInput
from crispy_forms.helper import FormHelper
from .models import Prints, Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category

        fields = ['name',]

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
            'limited_edition',
            'a5_price',
            'a4_price',
        ]
        widgets = {
            ''
        }


    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)


PRICE_CHOICES = (
        ('A5', 'A5'),
        ('A4', 'A4'),
    )


class PriceSelectionForm(forms.Form):
    
    selected_price = forms.ChoiceField(choices=PRICE_CHOICES, widget=forms.RadioSelect(attrs={'id': 'value'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
