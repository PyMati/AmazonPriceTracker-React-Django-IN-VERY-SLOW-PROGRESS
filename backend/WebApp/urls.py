from django.urls import path 
from . import views

urlpatterns = [
    path("dashboard", views.index, name = "index"),
    path("save-user", views.saveUser),
    path("show-user", views.showUsers)
]
