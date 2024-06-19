from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """ User profile form from user profile model """
    class Meta:
        model = UserProfile
        exclude = ('user', 'default_email',)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_city_or_town': 'City or Town',
            'default_county': 'County',
            'default_postcode': 'Postal Code',
        }
        # replace form labels with placehodlers
        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'rounded-1 profile-form-input'
            self.fields[field].label = False
