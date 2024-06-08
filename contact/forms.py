from django import forms
from crispy_forms.helper import FormHelper


class ContactForm(forms.Form):
    your_name = forms.CharField(max_length=80)
    email = forms.EmailField(max_length=254)
    subject = forms.CharField(max_length=80)
    message = forms.CharField(widget=forms.Textarea)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

