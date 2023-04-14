from django.urls import path

from . import views

urlpatterns = [
    path('menu', views.menu, name='menu'),
    path('management', views.management, name='management'),
    path('add_item/', views.add_item, name='add_item'),
    path('edit/<item_id>/', views.edit, name='edit'),
    path('delete-item/<item_id>/', views.delete_item, name='delete_item'),
]