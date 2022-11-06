from django.urls import path
from . import views

urlpatterns = [
    path('', views.janken, name='janken'),
]