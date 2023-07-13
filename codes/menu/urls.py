from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LoginView
from . import views
urlpatterns = [
    path('form/',views.form),
    path('', views.index,name='index'),
    path('error/', views.loginError,name= 'loginErr'),
    path('404/',views.Err404),
    path('login/', views.login,name='login'),
    path('loginError/', views.loginError),
    path('message/<int:stuID>/', views.message, name = 'message'),
    path('messageForm/', views.messageForm),
    path('selfForm/',views.selfFrom, name = 'selfForm'),
    path('sumbit/',views.submit, name = 'submit'),
    path('registerParse/', views.registerParse, name = 'registerParse'),
    path('loginParse/',views.loginParse, name='loginParse'),
    path('stuIndex/',views.std,name='std'),
    path('teaIndex/',views.tea,name='tea'),
    path('register/',views.register,name='register'),
]