from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.all_projects, name='projects'),
    path('wales/', views.wales, name='wales'),
]
