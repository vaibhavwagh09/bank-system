from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about_us', views.about_us, name="about_us"),
    path('users', views.users, name="users"),
    path('Add_users', views.Add_users, name="Add_users"),
    path('transactions', views.transactions, name="transactions"),
    path('payment/<str:pk>/', views.payment, name="payment")
]


