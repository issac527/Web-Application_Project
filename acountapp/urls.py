from django.contrib import admin
from django.urls import path, include

from acountapp.views import hello_world, AccountCreateView

app_name = 'acountapp'

urlpatterns = [
    path('hw/', hello_world, name = "hw"),
    path("create/", AccountCreateView.as_view(), name = "create")
]