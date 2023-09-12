

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.chat, name='index'),
    path("signup/",views.Signup,name='signup'),
    path('login/',views.Login,name="login"),
    path("logout/",views.Logout)
]
