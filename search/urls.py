from django.urls import path
from search.views import search

urlpatterns = [
    path('', search, name='Search Problem'),
]
