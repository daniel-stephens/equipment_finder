from django.urls import path

from .views import homepage, search, delete_data

urlpatterns = [
    path("", homepage, name='home'),
    path("search/", search, name='search'),
    path('delete_equipment/<str:pk>/', delete_data, name='delete')
]
