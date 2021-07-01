from django.contrib import admin
from django.urls import path, include

from acountapp.views import hello_world

app_name = 'acountapp'

urlpatterns = [
    path('hw/', hello_world, name = "hw")
]