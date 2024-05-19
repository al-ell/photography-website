from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.all_projects, name='all_projects'),
    path('add_project/', views.add_project, name='add_project'),
    path('add_photo/', views.add_photo, name='add_photo'),
    path('edit_project/<int:project_id>', views.edit_project, name='edit_project'),

    path('wales/', views.wales, name='wales'),
]
