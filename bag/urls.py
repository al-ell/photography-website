from django.urls import path
from . import views
""" Urls for the bag app """


urlpatterns = [
    path('', views.bag, name='bag'),
    path('add/<prints_id>/', views.add_to_bag, name='add_to_bag'),
    path('adjust/<prints_id>/', views.adjust_bag, name='adjust_bag'),
    path('remove/<prints_id>/', views.remove_from_bag, name='remove_from_bag'),
]
