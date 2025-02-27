from django.urls import path
from . import views
""" Urls for the about app """


urlpatterns = [
    path('', views.about, name='about'),
]
