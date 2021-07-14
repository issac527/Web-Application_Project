from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from acountapp.views import hello_world, AccountCreateView

app_name = 'acountapp'

urlpatterns = [
    path('hw/', hello_world, name = "hw"),
    path("create/", AccountCreateView.as_view(), name = "create"),
    path("login/", LoginView.as_view(template_name = "acountapp/login.html"), name = "login"),
    path("logout", LogoutView.as_view(), name = "logout")
]