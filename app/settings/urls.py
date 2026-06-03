from django.urls import path
from app.settings import views

urlpatterns = [
    path("", views.home, name="home"),
]
