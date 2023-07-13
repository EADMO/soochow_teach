from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LoginView
from . import views
urlpatterns = [
    path('form/',views.form),
    path('', views.login,name='login'),
    path('error/', views.loginError,name= 'loginErr'),
    path('404/',views.Err404),
    path('loginError/', views.loginError),
    path('message/<int:stuID>/', views.message, name = 'message'),
    path('messageForm/', views.messageForm,name='messageForm'),
    path('selfForm/',views.selfFrom, name = 'selfForm'),
    path('sumbit/',views.submit, name = 'submit'),
    path('stuSub',views.stuSub,name='stuSub'),
    path('registerParse/', views.registerParse, name = 'registerParse'),
    path('loginParse/',views.loginParse, name='loginParse'),
    path('stuIndex/',views.std,name='std'),
    path('teaIndex/',views.index,name='index'),
    path('register/',views.register,name='register'),
]