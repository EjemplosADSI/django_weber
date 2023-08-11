from django.urls import path

from . import views

urlpatterns = [
    # ex: /busine/
    path("", views.index, name="index"),
]
