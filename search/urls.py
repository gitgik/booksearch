"""Url pattern definitions for search app."""
from django.conf.urls import url
from .views import HomeView, SearchView
urlpatterns = [
    url(r'^', HomeView.as_view(), name="index"),
    url(r'^search/', SearchView.as_view(), name="search")
]
