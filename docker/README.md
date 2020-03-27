# Running the project
# Based on env_example create the .env file
cp env_example .env

# Create docker instance
docker-compose build

# Run docker instance
docker-compose up

# Access to the docker instance to admin the system
docker exec -it belvo-http bash

# Go to the api folder
cd belvoapi

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create super user (password used 1234567890)
python manage.py createsuperuser --email admin@example.com --username admin

# Browse http://localhost:8080/admin

# Test de api with Postman or curl
url: http://localhost:8080/api/transactions/add
method: post
body (json)
{
	"reference": "test3",
	"account": "test1",
	"date": "2030-12-10 12:22",
	"amount": 34.1,
	"type": "test1",
	"category": "test1",
	"user_id": 3
}

# --------------------------- #

# For testing purposes 0.0.0.0 is allowed and passwords are simple
# CSRF token was excepted for routes csrf_exempt

# TODO (pending, I would like to improve):
# check user age range and use date instead of integers
# change project name from blog_project to a better choice

# --------------------------- #
# Some useful commands

# Build the docker container
docker-compose build

# Run docker instances
docker-compose run

# Stop docker instances
docker-compose stop

# Access to the docker container
docker exec -it belvo-http bash


# --------------------------- #
# How I have create the project (create config dir, create "api" app dir)
django-admin startproject config .
django-admin startapp api


# --------------------------- #
# Steps I did to create the API and users app (similar with transactions)

# Create a folder for the project
mkdir belvo && cd belvo

# Create the project using the name api_project
django-admin startproject api_project .

# Create the app for User crud
python manage.py startapp users

# Add users app and rest_framework to api_project settings file api_project/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'users',
]

# Create the model for users at users/models.py
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
# Create the migrations and execute
python manage.py makemigrations
python manage.py migrate

# Add users to the admin page users/admin.py
from django.contrib import admin
from . models import User

admin.site.register(User)

# Create view to manage users users/views.py
from rest_framework import generics

from .models import User
from .serializers import UserSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@method_decorator(csrf_exempt, name='user')
def AddUser(request):
    payload = json.loads(request.body.decode("utf-8"))
    user = User.objects.create(
        name=payload["name"],
        email=payload["email"],
        age=payload["age"],
    )
    serializer = UserSerializer(user)
    # return HttpResponse(json.dumps(serializer), content_type="application/json")
    return HttpResponse(json.dumps(serializer.data), content_type="application/json")


# Add users serializer
from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'email', 'age', 'created_at', 'updated_at',)
        model = models.User

# Add user urls users/urls.py
# users/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('users/add', views.AddUser),
]

# Make user.urls available a api_project/urls.py
...
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
]

# Create the super user to have access to the admin page
python manage.py createsuperuser

# Run the server (using docker) to be able to browser http://localhost:8080/admin/
docker-compose up
