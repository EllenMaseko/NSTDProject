from django.urls import path, include
from . import views

urlpatterns = [
    #path("", views.home),
    path("", views.sneaker_predict, name="api_endpoint"),
]
