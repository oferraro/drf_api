# transactions/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('transactions/', views.TransactionList.as_view()),
    path('transactions/<int:pk>/', views.TransactionDetail.as_view()),
    path('transactions/add', views.AddTransaction),
]