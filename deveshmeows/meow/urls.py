from django.urls import path
from meow.views import home

urlpatterns = [
    path('index', home, name='home'),
]
