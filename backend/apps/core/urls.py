from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("gestor/", views.gestor_panel, name="gestor_panel"),
]