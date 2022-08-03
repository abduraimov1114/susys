import imp
from django.urls import path
from .views import home, example


urlpatterns = [
    path('', home),
    path('example/', example)
]
