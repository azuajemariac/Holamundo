from django.urls import path
from app1.views import hola_mundo, adios_mundo


urlpatterns =[
    path('',hola_mundo),
    path('app1',adios_mundo.as_view()),
]