from django.urls import path
from django.contrib.auth import views as auth_views

from . import views #convention

urlpatterns = [
    path('', views.index),
    path('food/', views.get_food),
]