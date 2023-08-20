from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("/world", views.world, name="world"),
    path("/python", views.python, name="python"),
    path("/<str:name>", views.greet, name="greet"),
]