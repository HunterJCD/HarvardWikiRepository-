from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("createnewpage", views.createnewpage, name="createnewpage"),
    path("RandomPage", views.RandomPage, name="RandomPage"),
    path("search", views.search, name="search"),
    path("editpages/<str:title>", views.editpages, name="editpages"),
    path("wiki/<str:title>", views.wiki, name="wiki")
]
