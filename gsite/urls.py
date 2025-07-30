from django.urls import path
from gsite import views

urlpatterns = [
    path("", views.index, name="index"),
    path('cli/', views.cli, name='cli'),
    path('web/', views.web, name='web'),
    path('blog/', views.blog, name='blog'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
]