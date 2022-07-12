from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("createnewpage", views.createnewpage, name="createnewpage"),
    path("wiki/<str:title>", views.wiki, name="wiki")
]
