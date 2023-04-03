from django.urls import path

from . import views

urlpatterns = [
    path('wines', views.wines, name='wines'),
]