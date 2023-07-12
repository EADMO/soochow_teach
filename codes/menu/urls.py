from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [
    path('form/',views.form),
    path('', views.index),
    path('404/',views.Err404),
    path('login', views.login),
    path('message/<int:stuID>/', views.message),
    path('messageForm/', views.messageForm),
    path('selfForm/',views.selfFrom)
]