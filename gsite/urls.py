from django.urls import path
from gsite import views

urlpatterns = [
    path("", views.index, name="index"),
]