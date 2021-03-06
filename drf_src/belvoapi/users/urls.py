# users/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('users/add', views.AddUser),
    path('users/balance', views.UserBalance),
]