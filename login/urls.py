from django.urls import path

from login.views import (
    indexView,
    mainView,
)

urlpatterns = [
    path('', indexView, name='index'),
    path('main/', mainView, name='main'),
]