from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:bus_id>", views.bus, name="bus"),
    path("<str:bus_id>/book", views.book, name="book")
]