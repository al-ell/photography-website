from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
""" Urls for the about app """


urlpatterns = [
    path('', views.about, name='about'),
]
