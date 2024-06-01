from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'city_or_town', 'county', 'postcode', 'country',)

    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'city_or_town': 'City or Town', 
            'county': 'County',
            'postcode': 'Postal Code',
            'country': 'Country'
        }
    

