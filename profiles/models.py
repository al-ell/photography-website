from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """ User profile model """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_email = models.EmailField(max_length=254, null=True,
                                      blank=True)
    default_phone_number = models.CharField(max_length=20, null=True,
                                            blank=True)
    default_street_address1 = models.CharField(max_length=100, null=True,
                                               blank=True)
    default_street_address2 = models.CharField(max_length=100, null=True,
                                               blank=True)
    default_city_or_town = models.CharField(max_length=40, null=True,
                                            blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_county = models.CharField(max_length=40, null=True, blank=True)
    default_country = CountryField(blank_label='Country',
                                   null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):

    if created:
        UserProfile.objects.create(user=instance)

    instance.userprofile.save()
