from django.contrib import admin
from django.urls import path

from . import views

app_name = "main"
urlpatterns = [
    path('',views.homepage,name="home"),
    path('login/',views.login_request,name="login"),
    path('signup/',views.sign_up,name="signup"),
    path('logout/', views.logout_request, name="logout"),
]