from django import forms
from django.core.validators import EmailValidator
from crispy_forms.helper import FormHelper


class ContactForm(forms.Form):
    """ Contact form """
    your_name = forms.CharField(max_length=80)
    email = forms.CharField(max_length=254, validators=[EmailValidator()])
    subject = forms.CharField(max_length=80)
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
