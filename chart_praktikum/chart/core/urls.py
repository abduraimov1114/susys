from multiprocessing import context
from django.urls import path
from .views import example, home 

urlpatterns = [
    path('', home),
    path('example/', example)
    
]
