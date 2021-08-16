from django.urls import path
from . import views
#list, get, save entry in util.py

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:entryKey>", views.view_entry, name="view"),
    path("search/", views.search, name="search"),
    path("new/", views.new, name="new"),
    path("add/", views.add, name ="add"),
    path("editPage/<str:entryKey>", views.editPage, name ="editPage"),
    path("saveEdit/<str:entryKey>", views.saveEdit, name="saveEdit"),
    path("random/", views.randomPage, name="random")
]
