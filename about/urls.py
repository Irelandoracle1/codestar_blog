from django.urls import path
from . import views

urlpatterns = [
    path("", views.about_me, name="about"),  # <-- match the view name
]
