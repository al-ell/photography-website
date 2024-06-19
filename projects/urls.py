from django.urls import path
from . import views


urlpatterns = [
    path('', views.portfolio_admin, name='portfolio_admin'),
    path('add_project/', views.add_project, name='add_project'),
    path('add_photo/', views.add_photo, name='add_photo'),
    path('edit_project/<int:project_id>', views.edit_project,
         name='edit_project'),
    path('edit_photo/<int:photo_id>', views.edit_photo, name='edit_photo'),
    path('delete_project/<int:project_id>', views.delete_project,
         name='delete_project'),
    path('delete_photo/<int:photo_id>', views.delete_photo,
         name='delete_photo'),
    path('wales/', views.wales, name='wales'),
    path('discovery/', views.discovery, name='discovery'),
]
