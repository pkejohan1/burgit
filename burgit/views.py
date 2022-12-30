from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User, Toplist, BurgerPlace

# Create your views here.
def index(request):
  template = loader.get_template('test.html')
  return HttpResponse(template.render())

def users(request):
  users = User.objects.all()
  template = loader.get_template('users.html')
  context = {
    'users': users,
  }
  return HttpResponse(template.render(context, request))

def places(request):
  places = BurgerPlace.objects.all()
  template = loader.get_template('places.html')
  context = {
    'places': places
  }
  return HttpResponse(template.render(context, request))

def sayHi():
  return HttpResponse('Hi!')

def sayHello():
  return HttpResponse('Hello!')

