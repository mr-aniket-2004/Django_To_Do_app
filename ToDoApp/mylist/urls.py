from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("add/", views.add_task, name="add_task"),
    path("edit/", views.edit_task, name="edit_task"),
    path("delete/<int:list_id>/", views.delete_task, name="delete_task"),
]
