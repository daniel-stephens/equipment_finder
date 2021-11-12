from django.urls import path
from django.urls.resolvers import URLPattern

from .views import homepage, search

urlpatterns = [
    path("", homepage, name='home'),
    path("search/", search, name='search')
]