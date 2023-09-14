from django.urls import path

from login.views import (
    indexView,
)

urlpatterns = [
    path('', indexView, name='index'),
]