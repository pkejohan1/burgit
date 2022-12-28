from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='hej'),
  path('users', views.users, name='users'),
  path('places', views.places, name='places')
]