from django.contrib import admin
from django.urls import path ,include
from home import views

urlpatterns = [
   path('',views.index,name="home"),
   path('login',views.loginUser,name="login"),
   path('signin',views.signin,name='signin'),
   path('logout',views.logoutuser,name='logout'),
]