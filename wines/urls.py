from django.urls import path

from . import views

urlpatterns = [
    path('wines', views.wines, name='wines'),
    path('wine_management', views.wine_management, name='wine_management'),
    path('add_wine/', views.add_wine, name='add_wine'),
    path('edit_wine/<item_id>/', views.edit_wine, name='edit_wine'),
    path('delete-wine/<item_id>/', views.delete_wine, name='delete_wine'),
]
